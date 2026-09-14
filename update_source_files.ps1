# adjust: relative path to crimson_driver
$baseDir = "../../gitlab"

$sourceFiles = @(
    "ndigo_driver/include/ndigo_common_interface.h",
    "ndigo_driver/include/ndigo_interface.h",
    "crono_dma_driver/include/crono_interface.h"
)

$destDirs = @(
    ".",
    ".",
    "."
)

# Validate input lengths
if ($sourceFiles.Count -ne $destDirs.Count) {
    Write-Error "Source and destination lists must have the same number of items."
    exit 1
}

# Loop and copy
for ($i = 0; $i -lt $sourceFiles.Count; $i++) {
    $relativePath = $sourceFiles[$i]
    $src = Join-Path $baseDir $relativePath
    $destDir = $destDirs[$i]

    $fileName = Split-Path $relativePath -Leaf
    $destPath = Join-Path $destDir $fileName

    # Ensure destination directory exists
    if (!(Test-Path $destDir)) {
        New-Item -ItemType Directory -Path $destDir -Force | Out-Null
    }

    # Copy file
    Copy-Item -Path $src -Destination $destPath -Force

    Write-Host "Copied $src -> $destPath"
}
