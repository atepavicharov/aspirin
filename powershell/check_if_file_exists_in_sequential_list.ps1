[datetime] $startDate = "2020-10-13"
[datetime] $endDate = "2021-11-07"
$fileDateFormat = "yyyyMMdd"
$suffix = "_LOAN_DATA.csv"
$path = "D:\Downloads\Cash Shop\Init Import\"

while($startDate -le $endDate)
{
    $fullPath = $path+$startDate.ToString($fileDateFormat)+$suffix

    if(!(Test-Path -Path $fullPath -PathType Leaf)) {
        Write-Host -ForegroundColor Magenta "$($startDate.ToString("yyyy-MM-dd")) is missing !"
    }else{
        # Uncomment the following line if you want to see found files !
        # Write-Host -ForegroundColor Green "$($fullPath) found!"
        }
    $startDate = $startDate.AddDays(1)
}
