$fileName = Get-ChildItem "<path_to_folder>\"

$fileName | ForEach-Object {
    Write-Host $_.FullName
    $fullname = $_.FullName
    (Get-Content $fullname) -replace '\$','' | Set-Content $fullname
}
