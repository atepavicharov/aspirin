$logo = "
  ______ _ _        _____           _             
 |  ____(_) |      |  __ \         | |            
 | |__   _| | ___  | |  | | ___  __| |_   _ _ __  
 |  __| | | |/ _ \ | |  | |/ _ \/ _` | | | | '_ \ 
 | |    | | |  __/ | |__| |  __/ (_| | |_| | |_) |
 |_|    |_|_|\___| |_____/ \___|\__,_|\__,_| .__/ 
                                           | |    
                                           |_|  
"
Write-Host -ForegroundColor Green $logo

$mainDir = Read-Host "Please enter directory"
$logFile = "$($env:USERPROFILE)\Desktop\CheckForDuplicates_Result.txt"


if (Test-Path $logFile) {
  Remove-Item $logFile
}

Add-Content -Path $logFile -Value ($logo+"`nLog File Created on:"+(Get-Date)+"`n-----")

Get-ChildItem $($mainDir) -Recurse -PipelineVariable files | 
where { ! $_.PSIsContainer} | 
Group-Object -Property Name -PipelineVariable grp |
Where-Object {$_.Count -gt 1} |
ForEach-Object {
    Write-Host -ForegroundColor Magenta $_.Count "|" $_.Name 
    Add-Content -Path $logFile -Value ("$($_.Count) | $($_.Name)")
    
    foreach ($dir in ($_.Group).Directory) {
        Write-Host -ForegroundColor Gray `t`t$dir
        Add-Content -Path "$($env:USERPROFILE)\Desktop\CheckForDuplicates_Result.txt" -Value ("`t`t$($dir)")
    }
}

Write-Host ""
Write-Host -ForegroundColor Green "Job Done. Pres Enter to close!"
Read-Host ":"
