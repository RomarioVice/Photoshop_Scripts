import os, sys

from tempfile import mkdtemp
from photoshop import Session

def save_tiff(output_path=os.path.abspath(os.path.dirname(sys.argv[0]))):
	
	output_path = output_path or os.path.join(mkdtemp(prefix="_print"), "print.tiff")

	with Session() as ps:

		orig_name = ps.active_document.name
		print_name = f"{orig_name}_print"

		
		print_doc = ps.active_document.duplicate(print_name)
		print_doc.Flatten()
		print_doc.saveAs(output_path, ps.TiffSaveOptions(), TiffEncodingType.TIFFLZW)
		print_doc.close()
        
		return output_path

if __name__ == "__main__":
	print_file = save_tiff()
	print("\n")
	print("\n")
	print("\n")
	print("\n")
	print(f"乁( ◔ ౪◔)「 Tiff file saved to {print_file} ┑(￣Д ￣)┍")
	print("\n")
	print("\n")
	print("\n")
	print("\n")