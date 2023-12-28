import customtkinter
import os
from PIL import Image
import tkinter

from manipula import Util, ManipulaImagem

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.manipulaImagem = ManipulaImagem(Util())
        self.imagem1 = None
        self.title("Aplica filtro em imagem")
        self.geometry("800x550")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        main_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Bilateral_Filter.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Image Example", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Aplica Filtros",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Resultados",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")


        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        url_var = tkinter.StringVar()
        self.home_frame_entry = customtkinter.CTkEntry(self.home_frame, placeholder_text="URL", width=500, height=30, textvariable=url_var)
        self.home_frame_entry.grid(row=1, column=0, padx=20, pady=10)
        self.home_frame_button_download = customtkinter.CTkButton(self.home_frame, text="Download", image=self.image_icon_image, compound="right", command=self.faz_download)
        self.home_frame_button_download.grid(row=2, column=0, padx=20, pady=10)

        self.home_frame_msg_label = customtkinter.CTkLabel(self.home_frame, text="Clique no botão para fazer o download da imagem.")
        self.home_frame_msg_label.grid(row=3, column=0, padx=20, pady=10)

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        selected_image = customtkinter.CTkImage(Image.open(os.path.join(main_path, "armando.jpeg")), size=(500, 350))
        self.second_frame_large_image_label = customtkinter.CTkLabel(self.second_frame, text="", image=selected_image)
        self.second_frame_large_image_label.grid(row=0, column=0, padx=10, pady=10)

        self.second_frame_button_f1 = customtkinter.CTkButton(self.second_frame, text="Gray Scale", image=self.image_icon_image, compound="right", command=self.aplica_gray_scale)
        self.second_frame_button_f1.grid(row=1, column=0, padx=20, pady=10)

        self.second_frame_button_f2 = customtkinter.CTkButton(self.second_frame, text="Black and White", image=self.image_icon_image, compound="right", command=self.aplica_preto_branco)
        self.second_frame_button_f2.grid(row=2, column=0, padx=20, pady=10)

        self.second_frame_button_f3 = customtkinter.CTkButton(self.second_frame, text="Cartoon", image=self.image_icon_image, compound="right", command=self.aplica_cartoon)
        self.second_frame_button_f3.grid(row=3, column=0, padx=20, pady=10)

        # create third frame
        #self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        self.third_frame = customtkinter.CTkScrollableFrame(self, corner_radius=0, fg_color="transparent")
        image_f1 = customtkinter.CTkImage(Image.open(os.path.join(main_path, "armando.jpeg")), size=(500, 350))
        image_f2 = customtkinter.CTkImage(Image.open(os.path.join(main_path, "armando.jpeg")), size=(500, 350))
        image_f3 = customtkinter.CTkImage(Image.open(os.path.join(main_path, "armando.jpeg")), size=(500, 350))

        self.third_frame_large_image_label_f1 = customtkinter.CTkLabel(self.third_frame, text="", image=image_f1)
        self.third_frame_large_image_label_f1.grid(row=0, column=0, padx=10, pady=10)

        self.third_frame_large_image_label_f2 = customtkinter.CTkLabel(self.third_frame, text="", image=image_f2)
        self.third_frame_large_image_label_f2.grid(row=1, column=0, padx=10, pady=10)

        self.third_frame_large_image_label_f3 = customtkinter.CTkLabel(self.third_frame, text="", image=image_f3)
        self.third_frame_large_image_label_f3.grid(row=2, column=0, padx=10, pady=10)

        # select default frame
        self.select_frame_by_name("home")

    def aplica_gray_scale(self):
        self.manipulaImagem.aplica_filtro_grayscale(minha_imagem=self.imagem1, nome='armando')

    def aplica_preto_branco(self):
        self.manipulaImagem.aplica_filtro_black_and_white(minha_imagem=self.imagem1, nome='armando')

    def aplica_cartoon(self):
        self.manipulaImagem.aplica_filtro_edges(minha_imagem=self.imagem1, nome='armando')

    def faz_download(self):
        try:
            self.home_frame_msg_label.configure(text="Aguarde...")
            my_link = self.home_frame_entry.get()
            # Cria uma imagem
            self.imagem1 = self.manipulaImagem.cria_imagem(minha_url=my_link)
            if self.imagem1: 
                self.home_frame_msg_label.configure(text="Download concluído!")
                self.home_frame_entry.delete(0, len(my_link))
                
        except Exception as ex:
            print(f'Erro: {str(ex)}')
            self.home_frame_msg_label.configure(text=f'Erro: {str(ex)}')

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")
    
    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")


if __name__ == "__main__":
    app = App()
    app.mainloop()