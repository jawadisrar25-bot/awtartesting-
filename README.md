# Awtar United Catering Services

PHP 8.2+, MySQL and Apache application for Awtar United. The public web root is `public/`. The other directories contain application code, CLI tools and installation files. Quotation and contact submissions save the inquiry and email queue entries in the same database transaction. A scheduled CLI worker sends messages through SMTP.

## Requirements

- PHP 8.2 or later with PDO MySQL, mbstring, fileinfo and OpenSSL
- MySQL 8 or a compatible MariaDB release, with InnoDB and UTF-8 support
- Composer and access to install dependencies
- Apache with mod_rewrite, mod_headers and override support for the directives in `public/.htaccess`
- PHP upload limit at least 5 MB per file. Use a 55 MB POST limit if enabling ten-image batches. Set MySQL max_allowed_packet above 5 MB.
- SMTP account, verified sender, HTTPS certificate and a cron scheduler

## Local installation and XAMPP

1. Unzip the project into a private folder such as `C:\awtar-united`. Preserve hidden files. Start Apache and MySQL from the XAMPP Control Panel.
2. Open a terminal in the project folder. With XAMPP's PHP available on PATH, run `composer install --no-dev --optimize-autoloader`.
3. Import `database/awtar_united.sql` through phpMyAdmin or run `mysql -u root -p < database/awtar_united.sql`. Use this installation script against a fresh database. Create a dedicated application database account with SELECT, INSERT, UPDATE and DELETE privileges on the application database.
4. Copy `.env.example` to `.env`. Set the database host, database name, username and password. For XAMPP set `APP_URL=http://awtar.local`. Set your actual sender settings before processing email.
5. Add `127.0.0.1 awtar.local` to the operating system hosts file. Enable Apache virtual hosts and use a host like the following. Restart Apache.
   
   ```apache
   <VirtualHost *:80>
       ServerName awtar.local
       DocumentRoot "C:/awtar-united/public"
       <Directory "C:/awtar-united/public">
           AllowOverride All
           Require all granted
       </Directory>
   </VirtualHost>
   ```
6. Run `php bin/create-admin.php owner@example.com` using your own address. Type a unique 12–72-byte password on standard input and press Enter. The terminal may echo typed characters. Use a private terminal.
7. Open `http://awtar.local/` for the public site or `http://awtar.local/admin/` for admin.
8. For a developer-only server using the same database, set `APP_URL=http://localhost:8000` and use `php -S localhost:8000 -t public router.php`.

## cPanel deployment

1. Back up the current site, database, and official media. Test under a staging hostname before changing the production document root.
2. Put the project outside `public_html` and point the domain or staging domain's document root at the project's `public/` directory. If the host locks that setting, ask the host to set it. Keep `.env`, Composer libraries, SQL and CLI files outside the web root.
3. Choose PHP 8.2 or newer for Apache and CLI. Install dependencies over SSH or build `vendor/` with Composer on a compatible host and upload it alongside the application.
4. Create the database and account through cPanel. If cPanel prefixes the database name, remove the first two lines from a copy of the SQL file and import into the selected database. Update the DSN to match.
5. Set `APP_URL` to the HTTPS address and restrict access to `.env` to your hosting account. Set up HTTPS through AutoSSL or your hosting provider. Create the first owner and configure email.
6. Preserve `/logo1.png` and `/images/` from the current site before switching the live domain. The seed data references those official live URLs. Stage with the live assets still reachable. You can also replace each URL with an approved HTTPS asset or upload a replacement via the relevant admin module. Review and approve third-party client logos before publishing.
7. Test the full acceptance list below with controlled records before switching live traffic. Keep an offsite database backup with access controls. Backups contain customer information, uploaded attachments and email queue data.

## SMTP and mail delivery

Set `SMTP_HOST`, `SMTP_PORT`, `SMTP_ENCRYPTION` (`tls` for STARTTLS or `smtps` for implicit TLS), `SMTP_USER`, `SMTP_PASSWORD` and `SMTP_FROM`. Use a sender verified by your provider and set the required DNS records. Keep credentials in `.env` or your host's environment configuration.

Set internal and optional secondary notification recipients in the admin area. `info@awtarksa.com` is seeded. Enable customer confirmations and status emails as required. On staging, change the internal recipient to a test inbox before sending. Run `php bin/send-email.php` and verify a real internal notification and customer confirmation in the intended test inboxes. The logs report SMTP acceptance or failure. An SMTP acceptance can precede final inbox delivery.

Configure a cPanel cron job once per minute using the correct PHP executable:

```cron
* * * * * /path/to/php /home/account/awtar-united/bin/send-email.php
```

The worker retries failed messages up to five total attempts, with a 15-minute delay between failures. An owner can requeue failed messages through Email. If the process is interrupted after the SMTP provider accepts a message and before the database update, that message can be sent again.

## Content and launch checks

- Confirm the official logo and images load at their final URLs. The installation seeds real company-site photography, public project references and the publicly listed Riyadh service-area map. Enter an exact office map embed after Awtar confirms its pin.
- Add approved menus, item photographs and optional prices through Admin → Menus. Menu categories are seeded without invented dishes or prices. Publish additional gallery images and testimonials only after approval. Seeded service copy is based on the supplied brief.
- Confirm the existing public phone number `+966 56 469 2511` and the requested WhatsApp number `+966 54 526 4145`.
- Load all menus and public routes at desktop and mobile sizes. Check navigation, filters, lightbox, image requests, business hours, sitemap, robots and WhatsApp links.
- Submit a contact inquiry and a quote with an attachment. Confirm that both appear in MySQL and in the dashboard. Re-submit the same form token and check the records have not duplicated. Review the unique reference, staff assignment, statuses, internal notes, CSV export and attachment permissions.
- Sign in under each role. Owner manages site settings, email, accounts and audit logs. Editor manages content and inquiries. Staff manages inquiries. Verify sign-out and password change. Check create, update, visibility and delete operations for each content module.
- Configure SMTP and confirm both real emails arrive. Review PHP, database and browser logs. Remove controlled test records from staging or start production on a fresh database.

Run the basic integration smoke test with the SMTP worker stopped and an isolated staging database. Use Python 3.9+ and run `python3 tests/smoke.py http://localhost:8000 owner@example.com`. The script creates inquiry and queue records. Delete the staging database before releasing to production or use a fresh production database.

## Content sources

Official site: https://awtarksa.com/  
Official contact details and service-area map: https://awtarksa.com/contact.html  
Official Instagram: https://www.instagram.com/awtarunited/
