# Get-Content and Measure-Object are fine for small files, but both are super inefficient with memory. 
# I had real problems with large files.

$fileName = Get-ChildItem "<path_to_folder>\"

$fileName | ForEach-Object {

    [int]$LinesInFile = 0
    $reader = New-Object IO.StreamReader $_.FullName
     while($reader.ReadLine() -ne $null){ $LinesInFile++ }

    Write-Host -ForegroundColor Magenta $_.FullName":"($LinesInFile-1) # removing the header

    $reader.Dispose()
}
