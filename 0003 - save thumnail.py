import os, sys
from tempfile import mkdtemp

from photoshop import Session

def create_thumbnail(output_path=os.path.abspath(os.path.dirname(sys.argv[0]))):
	
	"""Create a thumbnail image for currently active document.

    Args:
        output_path (str): The absolute output path of the thumbnail image.
            The default is to output to a temporary folder.
        max_resolution (int): The max resolution of the thumbnail. The default
            is `512`.

    Returns:
        str: The absolute output path of the thumbnail image.

    """

	output_path = output_path or os.path.join(mkdtemp(prefix="thumb"), "thumb.jpg")

	with Session() as ps:

		orig_name = ps.active_document.name
		thumb_name = f"{orig_name}_thumb"

		thumb_doc = ps.active_document.duplicate(thumb_name)
		thumb_doc.changeMode(2, [])
		thumb_doc.saveAs(output_path, ps.JPEGSaveOptions(), asCopy=True)
		thumb_doc.close()
        
		return output_path
		

if __name__ == "__main__":
	thumb_file = create_thumbnail()
	print("\n")
	print("\n")
	print("\n")
	print("\n")
	print(f"乁( ◔ ౪◔)「 Thumbnail file saved to {thumb_file} ┑(￣Д ￣)┍")
	print("\n")
	print("\n")
	print("\n")
	print("\n")