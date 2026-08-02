<!-- <?php
echo "<pre>";

echo "Current Directory: " . getcwd() . "\n\n";

echo "---- Files in Current Directory ----\n";
$current = scandir(".");
foreach ($current as $file) {
    if ($file != "." && $file != "..") {
        echo $file . "\n";
    }
}

echo "\n---- Files in Parent Directory ----\n";
$parent = scandir("..");
foreach ($parent as $file) {
    if ($file != "." && $file != "..") {
        echo $file . "\n";
    }
}

echo "</pre>";
?> -->