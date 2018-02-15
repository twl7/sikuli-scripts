
function populate_png_manifest($directory){
	$txt_file =  $directory + "\png_manifest";
	$null > $txt_file
	$L = Resolve-Path $directory | %{$_.Path.length + 1}
	get-childitem -Recurse $directory *.png | ForEach-Object {
		$relative_path = $_.FullName.substring($L);
		$constant = $relative_path.replace("\","_").split(".")[0].ToUpper();
		echo "$constant $relative_path" | Out-File -Encoding Unicode -append $txt_file
		}
	
}

get-childitem -recurse . *.png | ? -FilterScript {$_.Name -match "^\d+.png"} | rm
get-childitem -directory . | %{$directory = $_.Name; populate_png_manifest($directory)}