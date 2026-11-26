<?php
$path=parse_url($_SERVER['REQUEST_URI'],PHP_URL_PATH);
if (preg_match('~^/(index|about|services|menus|gallery|events|contact|get-quote)\.html$~D',$path,$matches)) {
    require __DIR__.'/public/'.$matches[1].'.php';
    return true;
}
if ($path==='/sitemap.xml' || $path==='/robots.txt') {
    require __DIR__.'/public/'.explode('.',substr($path,1))[0].'.php';
    return true;
}
return false;
