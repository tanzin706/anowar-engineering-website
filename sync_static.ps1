<# 
Automate static export and local sync.

Steps performed:
1) Run the Django export to regenerate static_site (uses your venv).
2) Mirror static_site into a separate static repo folder for upload.

Customize STATIC_SITE_TARGET via environment variable if you keep the static repo elsewhere.
#>

$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$python = Join-Path $root ".venv\Scripts\python.exe"
$manage = Join-Path $root "manage.py"
$source = Join-Path $root "static_site"

# Destination for the static repo (override with $env:STATIC_SITE_TARGET)
$target = if ($env:STATIC_SITE_TARGET) { $env:STATIC_SITE_TARGET } else { "D:\Anowar Engineering Static Website" }

if (-not (Test-Path $python)) {
    Write-Error "Python venv not found at $python. Activate or create .venv first."
}

# 1) Export static site
& $python $manage export_static

# 2) Sync to target static repo (if it exists)
if (-not (Test-Path $target)) {
    Write-Warning "Target path '$target' not found. Skipping copy. Set STATIC_SITE_TARGET or create the folder."
    exit 0
}

if (-not (Test-Path $source)) {
    Write-Error "Source static_site not found at $source"
}

robocopy $source $target /MIR /XD .git /R:2 /W:2 /NFL /NDL | Out-Null

if ($LASTEXITCODE -gt 3) {
    Write-Error "robocopy failed with code $LASTEXITCODE"
} else {
    Write-Host "Synced static export to '$target'."
}
