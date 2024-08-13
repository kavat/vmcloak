Write-host Uninstall software not needed

Get-AppxPackage *MicrosoftEdge* | Remove-AppxPackage
