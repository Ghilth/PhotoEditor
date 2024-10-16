import gradio as gr
from PIL import Image, ImageFilter  



# Images manipulation functions

#image resizing
def resize_image(image, width, height):
    '''Resizing is doing by using PIL resizing method'''

    return image.resize((width, height))



#image rotation
def rotate_image(image, angle):
    '''Rotation is doing by using PIL rotation method'''

    return image.rotate(angle)


#Edge Enhance
def edge_enhance(image):
    return image.filter(ImageFilter.EDGE_ENHANCE)

#Sharpen
def sharpen(image):
    return image.filter(ImageFilter.SHARPEN)

#Blur
def blur(image):
    return image.filter(ImageFilter.BLUR)

#SMOOTH
def smooth(image):
    return image.filter(ImageFilter.SMOOTH)

#contour
def contour(image):
    return image.filter(ImageFilter.CONTOUR)
                        
#3d
def emboss(image):
    return image.filter(ImageFilter.EMBOSS)








# Interface Gradio
def image_processing(image, operation, threshold=128, width=100, height=100, angle=0):
    
    if operation == "Resize":
        return resize_image(image, width, height)
    
    elif operation == "Rotate":
        return rotate_image(image, angle)
    
    elif operation == "Edge enhance":
        return edge_enhance(image)
    
    elif operation == "Sharpen":
        return sharpen(image)
    
    elif operation == "Blur":
        return blur(image)
    
    elif operation == "Contour":
        return contour(image)
    
    elif operation == "Emboss":
        return emboss(image)
    
    elif operation == "Smooth":
        return smooth(image)



    return image

   





#  Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("## Photo Editor")

    with gr.Row():
        image_input = gr.Image(type="pil", label="Load Image")
        operation = gr.Radio(["Resize", "Rotate","Sharpen","Blur","Contour","Emboss","Smooth","Edge enhance"], label="Opération")


        width = gr.Number(value=100, label="resizing width", visible=True)
        height = gr.Number(value=100, label="resizing height", visible=True)
        angle = gr.Number(value=0, label="rotation degree", visible=True)



    image_output = gr.Image(label="Final Image")

    submit_button = gr.Button("Apply")
    submit_button.click(image_processing, inputs=[image_input, operation,width, height, angle], outputs=image_output)


# Launch application
demo.launch()
