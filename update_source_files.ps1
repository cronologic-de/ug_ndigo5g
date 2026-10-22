$configFile = Join-Path $PSScriptRoot ".interface_source_locations"

if (-not (Test-Path $configFile)) {
    Write-Error "Config file '$configFile' not found."
    exit 1
}

$sourceFiles = Get-Content -Path $configFile | Where-Object { -not [string]::IsNullOrWhiteSpace($_) }

foreach ($src in $sourceFiles) {
    $resolvedSrc = if ([System.IO.Path]::IsPathRooted($src)) { $src } else { Join-Path $PSScriptRoot $src }

    if (-not (Test-Path $resolvedSrc)) {
        Write-Warning "Source file '$resolvedSrc' not found. Skipping."
        continue
    }

    $fileName = Split-Path $resolvedSrc -Leaf
    $destPath = Join-Path $PSScriptRoot $fileName

    Copy-Item -Path $resolvedSrc -Destination $destPath -Force
    Write-Host "Copied $resolvedSrc -> $destPath"
}
