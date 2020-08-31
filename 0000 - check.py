import os, sys
from photoshop import Session

def main():
	with Session() as ps:
		doc = ps.app.documents.add(29.7, 21)
		text_color = ps.SolidColor()
		text_color.rgb.red = 232
		text_color.rgb.green = 10
		text_color.rgb.blue = 224
		
		new_text_layer = doc.artLayers.add()
		new_text_layer.kind = ps.LayerKind.TextLayer
		new_text_layer.textItem.contents = 'Hello, World!'
		new_text_layer.textItem.position = [11.11, 9.7]
		new_text_layer.textItem.size = 40
		new_text_layer.textItem.color = text_color
		options = ps.JPEGSaveOptions(quality=5)
		path = os.path.abspath(os.path.dirname(sys.argv[0]))
		jpg = path + "\\" + sys.argv[1] 
		doc.saveAs(jpg, options, asCopy=True)
		# ps.app.doJavaScript(f'alert("save to jpg: {jpg}")')
		print("Save to jpg: " + path + "\\" + sys.argv[1])

if __name__ == "__main__":
	main()