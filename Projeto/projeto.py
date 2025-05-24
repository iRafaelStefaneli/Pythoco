import customtkinter as ctk
import customtkinter
from customtkinter import *
from customtkinter import CTkFrame
from tkinter import messagebox, PhotoImage
import tkinter as tk
from PIL import Image
#Declaração de Variaveis
Login = "admin"
Senha = "admin"
verificarmenu = 1
tipoaula = "Python"
numaula = 0
i = 0
#Definindo a função de Login

def Logar():
    ReceberLogin = entrada_login.get()
    ReceberLogin = ReceberLogin.lower()
    ReceberSenha = entrada_senha.get()
    ReceberSenha = ReceberSenha.lower()
    if Login == ReceberSenha and Senha == ReceberSenha:
        tellinicial.destroy()
        def py1atv():
            py1()
            quiz()
        def py2atv():
            py2()
            quiz()
        def py3atv():
            py3()
            quiz()
        def py1():
            global numaula
            tipoaula = "Python"
            numaula = 1
        def py2 ():
            global numaula
            tipoaula = "Python"
            numaula = 2
        def py3 ():
            global numaula
            tipoaula = "Python"
            numaula = 3
        def quiz():

                    

                    
                    global numaula
                    print(f"{numaula}")
                    #Python aula1
                    perguntaspythonal1 = ["O que o comando print('Python é incrível!') faz??","Qual destas opções representa uma variável em Python?","Qual é o resultado de 5 * 2 em Python?","Para fazer o usuário digitar o nome dele, usamos qual comando?","Uma pessoa de 16 anos usou um programa feito em Python\n que pergunta a idade e responde se ela pode ou não dirigir.\n O que o programa provavelmente vai dizer para essa pessoa?"]
                    Resps1alpy1 = ["Cria uma variável chamada Python","mensagem = 'Olá'","7","'print()'"," Que ela já pode dirigir"]
                    Resp2alpy1 = ["Exibe o texto “Python é incrível!” no computador"," print('mensagem')","10","'input()'","Que a idade está errada"]
                    Resp3alpy1 = ["Salva um arquivo com esse nome","var = print()","52","'def()'","Que ela ainda não pode tirar a carteira de motorista"]
                    Resp4alpy1 = ["Abre uma janela nova no navegador","input = 'mensagem'","Erro","'read()'","Nada, o programa vai fechar"]

                    perguntaspythonal2 =["O que o operador += faz em Python?","Qual operador lógico exige que as duas condições sejam verdadeiras?","Se uma condição if for falsa, qual estrutura pode ser usada para testar outra condição?","Qual operador lógico representa o 'contrário'?","O que acontece se nenhuma condição if ou elif for verdadeira?"]
                    Resps1alpy2 = ["Compara dois números","or","if","and","Executa o código dentro dentro deles"]
                    Resps2alpy2 = ["Subtrai um valor","not","elif","or","Executa o bloco else"]
                    Resps3alpy2 = ["Adiciona e atualiza o valor da variável","and","else","not","Volta para o início"]
                    Resps4alpy2 = ["Multiplica dois valores","igual","def","xor","Mostra erro"]

                    perguntaspythonal3 = ["O que é um laço de repetição?","Qual comando é usado para repetir enquanto uma condição for verdadeira?","No laço for, o que ele percorre?","O que acontece se não atualizarmos a variável dentro de um loop while?","No exemplo do laço for com vendas, o que o programa verifica?"]
                    Resps1alpy3 = ["Uma função para criar listas","for","Apenas números","O código roda mais rápido"," Se o dia da semana é sábado"]
                    Resps2alpy3 = [" Um comando que executa ações repetidamente","repeat","Sequências como listas, strings e ranges","O loop nunca começa","Se a venda está acima ou abaixo da meta"]
                    Resps3alpy3 = [" Uma variável temporária","while","Arquivos do computador"," O código dá erro automaticamente","O loop pode se tornar infinito"," Se a senha está correta"]
                    Resps4alpy3 = ["Um erro no código","loop","Apenas variáveis booleanas","nenhuma das alternativas","Se há erros no código"]

                    quiz = ctk.CTkToplevel()
                    pythocosurpreso = Image.open("imgs/pythoco_surpreso.png")
                    pysurpreso = CTkImage(pythocosurpreso,size=(100,120))
                    i=0
                    def analisarrespostaal1py():
                        global i
                        i = 0
                        perguntasver = perguntaspythonal1[i]
                        perguntaanalise = perguntasver
                        resposta = cbbescolhaalt.get()
                        if perguntaspythonal1[0] == perguntaanalise  and resposta == Resp2alpy1[0]:
                            print("Você acertou")
                            i += 1
                            lblresposta.configure(text = "Resposta certa",bg_color = "#000075")
                            quest1.configure(fg_color = "green")
                            perguntas.configure(text=f"{perguntaspythonal1[i]}")
                            cbbescolhaalt.configure(values=(Resps1alpy1[i],Resp2alpy1[i],Resp3alpy1[i],Resp4alpy1[i]))
                        elif perguntaspythonal1[0] == perguntaanalise  and resposta != Resp2alpy1[0]:
                            lblresposta.configure(text = "resposta errada",bg_color = "#000075")
                        elif perguntaspythonal1[1] == perguntaanalise  and resposta == Resps1alpy1[1]:
                            print("Você acertou")
                            i += 1
                            quest2.configure(fg_color = "green")
                            perguntas.configure(text=f"{perguntaspythonal1[i]}")
                            cbbescolhaalt.configure(values=(Resps1alpy1[i],Resp2alpy1[i],Resp3alpy1[i],Resp4alpy1[i]))
                        elif perguntaspythonal1[1] == perguntaanalise  and resposta != Resps1alpy1[1]:
                            lblresposta.configure(text = "Resposta certa",bg_color = "#000075")
                        elif perguntaspythonal1[2] == perguntaanalise  and resposta == Resp2alpy1[2]:
                            lblresposta.configure(text = "Resposta certa",bg_color = "#000075")
                            i += 1
                            quest3.configure(fg_color = "green")
                            perguntas.configure(text=f"{perguntaspythonal1[i]}")
                            cbbescolhaalt.configure(values=(Resps1alpy1[i],Resp2alpy1[i],Resp3alpy1[i],Resp4alpy1[i]))
                        elif perguntaspythonal1[2] == perguntaanalise  and resposta != Resp2alpy1[2]:
                            lblresposta.configure(text = "resposta errada",bg_color = "#000075")
                        elif perguntaspythonal1[3] == perguntaanalise  and resposta == Resp2alpy1[3]:
                            lblresposta.configure(text = "Resposta certa",bg_color = "#000075")
                            i += 1
                            quest4.configure(fg_color = "green")
                            perguntas.configure(text=f"{perguntaspythonal1[i]}")
                            cbbescolhaalt.configure(values=(Resps1alpy1[i],Resp2alpy1[i],Resp3alpy1[i],Resp4alpy1[i]))
                        elif perguntaspythonal1[3] == perguntaanalise  and resposta != Resp2alpy1[3]:
                            lblresposta.configure(text = "resposta errada",bg_color = "#000075")
                        elif perguntaspythonal1[4] == perguntaanalise  and resposta == Resp3alpy1[4]:
                            print("Você acertou")
                            i += 1
                            quest5.configure(fg_color = "green")
                            messagebox.showinfo("Final","Você completou o quiz parabens!")
                            lblresposta.configure(text = "Resposta certa",bg_color = "#000075")
                            quiz.destroy()
                        else:
                           lblresposta.configure(text = "resposta errada",bg_color = "#000075")
                    def analisarrespostaal2py():
                        global i
                        i = 0
                        perguntasver = perguntaspythonal2[i]
                        perguntaanalise = perguntasver
                        resposta = cbbescolhaalt.get()
                        if perguntaspythonal2[0] == perguntaanalise  and resposta == Resps3alpy2[0]:
                            print("Você acertou")
                            i += 2
                            lblresposta.configure(text = f"Resposta certa {i}",bg_color = "#000075")
                            quest1.configure(fg_color = "green")
                            perguntas.configure(text=f"{perguntaspythonal2[i]}")
                            cbbescolhaalt.configure(values=(Resps1alpy2[i],Resps2alpy2[i],Resps3alpy2[i],Resps4alpy2[i]))
                        elif perguntaspythonal2[0] == perguntaanalise  and resposta != Resps3alpy2[0]:
                            lblresposta.configure(text = f"Resposta errada {i}",bg_color = "#000075")
                        elif perguntaspythonal2[2] == perguntaanalise  and resposta == Resps2alpy2[2]:
                            print("Você acertou")
                            i += 1
                            quest3.configure(fg_color = "green")
                            lblresposta.configure(text = "Resposta certa",bg_color = "#000075")
                            perguntas.configure(text=f"{perguntaspythonal2[i]}")
                            cbbescolhaalt.configure(values=(Resps1alpy2[i],Resps2alpy2[i],Resps3alpy2[i],Resps4alpy2[i]))
                        elif perguntaspythonal2[2] == perguntaanalise  and resposta != Resps2alpy2[2]:
                            lblresposta.configure(text = "Resposta errada",bg_color = "#000075")
                        elif perguntaspythonal2[3] == perguntaanalise  and resposta == Resps3alpy2[3]:
                            print("Você acertou")
                            i += 1
                            quest4.configure(fg_color = "green")
                            lblresposta.configure(text = "Resposta certa",bg_color = "#000075")
                            perguntas.configure(text=f"{perguntaspythonal2[i]}")
                            cbbescolhaalt.configure(values=(Resps1alpy2[i],Resps2alpy2[i],Resps3alpy2[i],Resps4alpy2[i]))
                        elif perguntaspythonal2[3] == perguntaanalise  and resposta != Resps3alpy2[3]:
                            lblresposta.configure(text = "Resposta errada",bg_color = "#000075")
                        elif perguntaspythonal2[4] == perguntaanalise  and resposta == Resps2alpy2[4]:
                            print("Você acertou")
                            
                            quest5.configure(fg_color = "green")
                            messagebox.showinfo("Final","Você completou o quiz parabens!")
                            quiz.destroy()
                        else:
                            messagebox.showerror("?","Resposta incorreta ou invalida")
                            quiz.state("normal")
                    def analisarrespostaal3py():
                        global i
                        perguntasver = perguntaspythonal3[i]
                        perguntaanalise = perguntasver
                        resposta = cbbescolhaalt.get()
                        if perguntaspythonal3[0] == perguntaanalise  and resposta == Resps2alpy3[0]:
                            lblresposta.configure(text = "Resposta certa",bg_color = "#000075")
                            i += 1
                            quest1.configure(fg_color = "green")
                            perguntas.configure(text=f"{perguntaspythonal3[i]}")
                            cbbescolhaalt.configure(values=(Resps1alpy3[i],Resps2alpy3[i],Resps3alpy3[i],Resps4alpy3[i]))
                        elif perguntaspythonal3[0] == perguntaanalise  and resposta != Resps2alpy3[0]:
                            lblresposta.configure(text = "Resposta errada",bg_color = "#000075")
                        elif perguntaspythonal3[1] == perguntaanalise  and resposta == Resps3alpy3[1]:
                            print("Você acertou")
                            i += 1
                            quest2.configure(fg_color = "green")
                            lblresposta.configure(text = "Resposta certa",bg_color = "#000075")
                            perguntas.configure(text=f"{perguntaspythonal3[i]}")
                            cbbescolhaalt.configure(values=(Resps1alpy3[i],Resps2alpy3[i],Resps3alpy3[i],Resps4alpy3[i]))
                        elif perguntaspythonal3[1] == perguntaanalise  and resposta != Resps3alpy3[1]:
                            lblresposta.configure(text = "Resposta errada",bg_color = "#000075")
                        elif perguntaspythonal3[2] == perguntaanalise  and resposta == Resps2alpy3[2]:
                            print("Você acertou")
                            i += 1
                            quest3.configure(fg_color = "green")
                            lblresposta.configure(text = "Resposta certa",bg_color = "#000075")
                            perguntas.configure(text=f"{perguntaspythonal3[i]}")
                            cbbescolhaalt.configure(values=(Resps1alpy3[i],Resps2alpy3[i],Resps3alpy3[i],Resps4alpy3[i]))
                        elif perguntaspythonal3[2] == perguntaanalise  and resposta != Resps2alpy3[2]:
                            lblresposta.configure(text = "Resposta errada",bg_color = "#000075")
                        elif perguntaspythonal3[3] == perguntaanalise  and resposta == Resps3alpy3[3]:
                            print("Você acertou")
                            i += 1
                            quest4.configure(fg_color = "green")
                            lblresposta.configure(text = "Resposta certa",bg_color = "#000075")
                            perguntas.configure(text=f"{perguntaspythonal3[i]}")
                            cbbescolhaalt.configure(values=(Resps1alpy3[i],Resps2alpy3[i],Resps3alpy3[i],Resps4alpy3[i]))
                        elif perguntaspythonal3[3] == perguntaanalise  and resposta != Resps3alpy3[3]:
                            lblresposta.configure(text = "Resposta errada",bg_color = "#000075")
                        elif perguntaspythonal3[4] == perguntaanalise  and resposta == Resps2alpy3[4]:
                            print("Você acertou")
                            i ==0
                            quest5.configure(fg_color = "green")
                            messagebox.showinfo("Final","Você completou o quiz parabens!")
                            quiz.destroy()
                        else:
                            lblresposta.configure(text = f"resposta errada {i}")



                    quiz.config(background="#ffad2d")
                    quiz.title("QUIZ")
                    i = 0
                    perguntas = ctk.CTkLabel(quiz,bg_color="#000075",text=f"{perguntaspythonal1[0]}",font=("arial",18))
                    perguntas.grid()
                    frame_palavras = ctk.CTkFrame(quiz,height=100, width=400, corner_radius= 5,bg_color="#ffad2d",fg_color="#ffad2d")
                    frame_palavras.grid(sticky = "we")
                    quest1 = ctk.CTkLabel(frame_palavras,bg_color="#ffad2d",fg_color="cyan",text="",corner_radius=40)
                    quest1.grid(row = 1, column = 0,padx=25,sticky = "we")
                    quest2 = ctk.CTkLabel(frame_palavras,bg_color="#ffad2d",fg_color="cyan",text="",corner_radius=40)
                    quest2.grid(row = 1, column =2, padx = 25,sticky = "we")
                    quest3 = ctk.CTkLabel(frame_palavras,bg_color="#ffad2d",fg_color="cyan",text="",corner_radius=40)
                    quest3.grid(row = 1, column =3, padx = 25,sticky = "we")
                    quest4 = ctk.CTkLabel(frame_palavras,bg_color="#ffad2d",fg_color="cyan",text="",corner_radius=40)
                    quest4.grid(row = 1, column =4, padx = 25,sticky = "we")
                    quest5 = ctk.CTkLabel(frame_palavras,bg_color="#ffad2d",fg_color="cyan",text="",corner_radius=40)
                    quest5.grid(row = 1, column =5, padx = 25,sticky = "we")
                    boneco = ctk.CTkLabel(frame_palavras,image=pysurpreso,text="")
                    boneco.grid(row = 1, column = 9, sticky = "w", rowspan=2)
                    frame_alternativas = ctk.CTkFrame(quiz,height=100, width=400, corner_radius= 5, fg_color= "#ffad2d", bg_color="lightgreen")
                    frame_alternativas.grid(sticky = "w",row = 8)
                    cbbescolhaalt = customtkinter.CTkComboBox(frame_alternativas, values=(Resps1alpy1[i],Resp2alpy1[i],Resp3alpy1[i],Resp4alpy1[i]), width=400,button_color="#000075")
                    cbbescolhaalt.grid(column=1,row=1,columnspan =2,sticky = "ew")
                    btnanalisar = customtkinter.CTkButton(frame_alternativas,text="Analisar resposta",command=analisarrespostaal1py)
                    btnanalisar.grid(column =1, row=2, columnspan =2)
                    lblresposta = customtkinter.CTkLabel(quiz,text=" ",font=("arial", 15))
                    lblresposta.grid(column =1, row=3, columnspan =3)

                    if tipoaula == "Python" and numaula == 2:
                        i == 0
                        btnanalisar.configure(command=analisarrespostaal2py)
                        perguntas.configure(text=f"{perguntaspythonal2[i]}")
                        cbbescolhaalt.configure(values=(Resps1alpy2[i],Resps2alpy2[i],Resps3alpy2[i],Resps4alpy2[i]))
                    elif tipoaula == "Python" and numaula == 3:
                        i == 0
                        btnanalisar.configure(command=analisarrespostaal3py)
                        perguntas.configure(text=f"{perguntaspythonal3[i]}")
                        cbbescolhaalt.configure(values=(Resps1alpy3[i],Resps2alpy3[i],Resps3alpy3[i],Resps4alpy3[i]))
                    quiz.mainloop()
        def expansao():
            global verificarmenu
            verificarmenu = verificarmenu + 1
            framemenu1.configure(bg_color = "#ffad2d",fg_color="#000075")
            btnmenu.grid_configure(row=1,padx=(0,150))
            customtkinter.CTkLabel(framemenu1,text=(f"{verificarmenu}")).grid(row=2)
            btnaulas = customtkinter.CTkButton(framemenu1,text="Aulas",height=10,width=30,fg_color="#ffad2d",hover_color="#00cffc",command=expansao,font=("arial",18))
            btninfo = customtkinter.CTkButton(framemenu1,text="Sobre nós",height=10,width=30,fg_color="#ffad2d",hover_color="#00cffc",command=expansao,font=("arial",18))
            btnatv = customtkinter.CTkButton(framemenu1,text="Atividades",height=10,width=30,fg_color="#ffad2d",hover_color="#00cffc",command=quiz, font=("arial",18))
            btnaulas.grid(row = 3, pady = 18)
            btninfo.grid(row=4, pady = 18)
            btnatv.grid(row = 5, pady = (18,5))

            if verificarmenu >2:
                btnmenu.grid_configure(row=1,padx=(0,10))
                btnaulas.configure(width=30,height=1,fg_color = "#ffad2d", state = "disabled",text="        ")
                btninfo.configure(width=30,height=1,fg_color = "#ffad2d", state = "disabled",text="                ")
                btnatv.configure(width=30,height=1,fg_color = "#ffad2d", state = "disabled",text="                ")
                framemenu1.configure(bg_color = "#ffad2d",fg_color="#ffad2d")
                verificarmenu = 1
                customtkinter.CTkLabel(framemenu1,text=(f"{verificarmenu}")).grid(row=2)

                
                #definindo uma função para as aulas
        def aula1Python():
            def sairpy1():
                telmenu.state("zoomed")
                aula1.destroy()
            telmenu.state("icon")
            paginas = 0
            aula1 = ctk.CTkToplevel()
            aula1.state("zoomed")
            aula1.configure(fg_color = "#ffad2d")
            img1_aula1 = Image.open("imgs/aula1/img1.png")
            aula1img1 = CTkImage(img1_aula1,size=(1000,700))
            img2_aula1 = Image.open("imgs/aula1/img2.png")
            aula1img2 = CTkImage(img2_aula1,size=(1000,700))
            img3_aula1 = Image.open("imgs/aula1/img3.png")
            aula1img3 = CTkImage(img3_aula1,size=(1000,700))
            img4_aula1 = Image.open("imgs/aula1/img4.png")
            aula1img4 = CTkImage(img4_aula1,size=(1000,700))
            img5_aula1 = Image.open("imgs/aula1/img5.png")
            aula1img5 = CTkImage(img5_aula1,size=(1000,700))
            img6_aula1 = Image.open("imgs/aula1/img6.png")
            aula1img6 = CTkImage(img6_aula1,size=(1000,700))
            img7_aula1 = Image.open("imgs/aula1/img7.png")
            aula1img7 = CTkImage(img7_aula1,size=(1000,700))
            img8_aula1 = Image.open("imgs/aula1/img8.png")
            aula1img8 = CTkImage(img8_aula1,size=(1000,700))
            img9_aula1 = Image.open("imgs/aula1/img9.png")
            aula1img9 = CTkImage(img9_aula1,size=(1000,700))
            img10_aula1 = Image.open("imgs/aula1/img10.png")
            aula1img10 = CTkImage(img10_aula1,size=(1000,700))
            img11_aula1 = Image.open("imgs/aula1/img11.png")
            aula1img11 = CTkImage(img11_aula1,size=(1000,700))
            img12_aula1 = Image.open("imgs/aula1/img12.png")
            aula1img12 = CTkImage(img12_aula1,size=(1000,700))
            img13_aula1 = Image.open("imgs/aula1/img13.png")
            aula1img13 = CTkImage(img13_aula1,size=(1000,700))
            img14_aula1 = Image.open("imgs/aula1/img14.png")
            aula1img14 = CTkImage(img14_aula1,size=(1000,700))
            
            btsair = Image.open("imgs/saida_click.png")
            btsairimg = CTkImage(btsair, size=(25,25))
            



            aula1.state("icon")
            frameaulas = CTkScrollableFrame(aula1,width= 1000, height= 700)
            frameaulas.grid(rowspan = 18, columnspan = 5,column =25, pady = 10, padx = (150,220),sticky="e")
            Labelaula1 = CTkLabel(frameaulas,image=aula1img1,text="")
            Labelaula1.grid()
            Labelaula2 = CTkLabel(frameaulas,image=aula1img2,text="")
            Labelaula2.grid()
            Labelaula3 = CTkLabel(frameaulas,image=aula1img3,text="")
            Labelaula3.grid()
            Labelaula4 = CTkLabel(frameaulas,image=aula1img4,text="")
            Labelaula4.grid()
            Labelaula5 = CTkLabel(frameaulas,image=aula1img5,text="")
            Labelaula5.grid()
            Labelaula6 = CTkLabel(frameaulas,image=aula1img6,text="")
            Labelaula6.grid()
            Labelaula7 = CTkLabel(frameaulas,image=aula1img7,text="")
            Labelaula7.grid()
            Labelaula8 = CTkLabel(frameaulas,image=aula1img8,text="")
            Labelaula8.grid()
            Labelaula9 = CTkLabel(frameaulas,image=aula1img9,text="")
            Labelaula9.grid()
            Labelaula10 = CTkLabel(frameaulas,image=aula1img10,text="")
            Labelaula10.grid()
            Labelaula11 = CTkLabel(frameaulas,image=aula1img11,text="")
            Labelaula11.grid()
            Labelaula12 = CTkLabel(frameaulas,image=aula1img12,text="")
            Labelaula12.grid()
            Labelaula13 = CTkLabel(frameaulas,image=aula1img13,text="")
            Labelaula13.grid()
            Labelaula14 = CTkLabel(frameaulas,image=aula1img14,text="")
            Labelaula14.grid() 
            btnsair = customtkinter.CTkButton(aula1,image=btsairimg,text="sair",command=sairpy1)
            btnsair.grid(row=4,column=0,sticky="s",pady=(0,10))  
            aula1.mainloop()


        def aula2Python():
            def sairpy2():
                telmenu.state("zoomed")
                aula2.destroy()
            telmenu.state("icon")
            paginas = 0
            aula2 = ctk.CTkToplevel()
            aula2.state("zoomed")
            aula2.configure(fg_color = "#ffad2d")
            img1_aula2 = Image.open("imgs/aula2/img1.png")
            aula2img1 = CTkImage(img1_aula2,size=(1000,700))
            img2_aula2 = Image.open("imgs/aula2/img2.png")
            aula2img2 = CTkImage(img2_aula2,size=(1000,700))
            img3_aula2 = Image.open("imgs/aula1/img3.png")
            aula2img3 = CTkImage(img3_aula2,size=(1000,700))
            img4_aula2 = Image.open("imgs/aula2/img4.png")
            aula2img4 = CTkImage(img4_aula2,size=(1000,700))
            img5_aula2 = Image.open("imgs/aula2/img5.png")
            aula2img5 = CTkImage(img5_aula2,size=(1000,700))
            img6_aula2 = Image.open("imgs/aula2/img6.png")
            aula2img6 = CTkImage(img6_aula2,size=(1000,700))
            img7_aula2 = Image.open("imgs/aula2/img7.png")
            aula2img7 = CTkImage(img7_aula2,size=(1000,700))
            btsair = Image.open("imgs/saida_click.png")
            btsairimg = CTkImage(btsair, size=(25,25))
            aula2.state("icon")
            frameaulas = CTkScrollableFrame(aula2,width= 1000, height= 700)
            frameaulas.grid(rowspan = 18, columnspan = 5,column =25, pady = 10, padx = (150,220),sticky="e")
            Labelaula1 = CTkLabel(frameaulas,image=aula2img1,text="")
            Labelaula1.grid()
            Labelaula2 = CTkLabel(frameaulas,image=aula2img2,text="")
            Labelaula2.grid()
            Labelaula3 = CTkLabel(frameaulas,image=aula2img3,text="")
            Labelaula3.grid()
            Labelaula4 = CTkLabel(frameaulas,image=aula2img4,text="")
            Labelaula4.grid()
            Labelaula5 = CTkLabel(frameaulas,image=aula2img5,text="")
            Labelaula5.grid()
            Labelaula6 = CTkLabel(frameaulas,image=aula2img6,text="")
            Labelaula6.grid()
            Labelaula7 = CTkLabel(frameaulas,image=aula2img7,text="")
            Labelaula7.grid()
            btnsair = customtkinter.CTkButton(aula2,image=btsairimg,text="sair",command=sairpy2)
            btnsair.grid(row=4,column=0,sticky="s",pady=(0,10))  
            aula2.mainloop()

        def aula3Python():
            def sairpy3():
                telmenu.state("zoomed")
                aula3.destroy()
            telmenu.state("icon")
            paginas = 0
            aula3 = ctk.CTkToplevel()
            aula3.state("zoomed")
            aula3.configure(fg_color = "#ffad2d")
            img1_aula3 = Image.open("imgs/aula3/img1.png")
            aula3img1 = CTkImage(img1_aula3,size=(1000,700))
            img2_aula3 = Image.open("imgs/aula3/img2.png")
            aula3img2 = CTkImage(img2_aula3,size=(1000,700))
            img3_aula3 = Image.open("imgs/aula3/img3.png")
            aula3img3 = CTkImage(img3_aula3,size=(1000,700))
            img4_aula3 = Image.open("imgs/aula3/img4.png")
            aula3img4 = CTkImage(img4_aula3,size=(1000,700))
            img5_aula3 = Image.open("imgs/aula3/img5.png")
            aula3img5 = CTkImage(img5_aula3,size=(1000,700))
            img6_aula3 = Image.open("imgs/aula3/img6.png")
            aula3img6 = CTkImage(img6_aula3,size=(1000,700))
            img7_aula3 = Image.open("imgs/aula3/img7.png")
            aula3img7 = CTkImage(img7_aula3,size=(1000,700))
            img8_aula3 = Image.open("imgs/aula3/img8.png")
            aula3img8 = CTkImage(img8_aula3,size=(1000,700))
            btsair = Image.open("imgs/saida_click.png")
            btsairimg = CTkImage(btsair, size=(25,25))
            aula3.state("icon")
            frameaulas = CTkScrollableFrame(aula3,width= 1000, height= 700)
            frameaulas.grid(rowspan = 18, columnspan = 5,column =25, pady = 10, padx = (150,220),sticky="e")
            Labelaula1 = CTkLabel(frameaulas,image=aula3img1,text="")
            Labelaula1.grid()
            Labelaula2 = CTkLabel(frameaulas,image=aula3img2,text="")
            Labelaula2.grid()
            Labelaula3 = CTkLabel(frameaulas,image=aula3img3,text="")
            Labelaula3.grid()
            Labelaula4 = CTkLabel(frameaulas,image=aula3img4,text="")
            Labelaula4.grid()
            Labelaula5 = CTkLabel(frameaulas,image=aula3img5,text="")
            Labelaula5.grid()
            Labelaula6 = CTkLabel(frameaulas,image=aula3img6,text="")
            Labelaula6.grid()
            Labelaula7 = CTkLabel(frameaulas,image=aula3img7,text="")
            Labelaula7.grid()
            Labelaula8 = CTkLabel(frameaulas,image=aula3img8,text="")
            Labelaula8.grid()
            btnsair = customtkinter.CTkButton(aula3,image=btsairimg,text="sair",command=sairpy3)
            btnsair.grid(row=4,column=0,sticky="s",pady=(0,10))  
            aula3.mainloop()
        
        def aula4Infra():
            def sairInfra():
                telmenu.state("zoomed")
                aula4.destroy()
            telmenu.state("icon")
            paginas = 0
            aula4 = ctk.CTkToplevel()
            aula4.state("zoomed")
            aula4.configure(fg_color = "#ffad2d")
            img1_aula4 = Image.open("imgs/aula4/CAPA.jpg")
            aula4img1 = CTkImage(img1_aula4,size=(1000,700))
            img2_aula4 = Image.open("imgs/aula4/slide-1.jpg")
            aula4img2 = CTkImage(img2_aula4,size=(1000,700))
            img3_aula4 = Image.open("imgs/aula4/slide-2.jpg")
            aula4img3 = CTkImage(img3_aula4,size=(1000,700))
            img4_aula4 = Image.open("imgs/aula4/slide-3.jpg")
            aula4img4 = CTkImage(img4_aula4,size=(1000,700))
            img5_aula4 = Image.open("imgs/aula4/slide-4.jpg")
            aula4img5 = CTkImage(img5_aula4,size=(1000,700))
            img6_aula4 = Image.open("imgs/aula4/slide-5.jpg")
            aula4img6 = CTkImage(img6_aula4,size=(1000,700))
            img7_aula4 = Image.open("imgs/aula4/slide-6.jpg")
            aula4img7 = CTkImage(img7_aula4,size=(1000,700))
            img8_aula4 = Image.open("imgs/aula4/slide-7.jpg")
            aula4img8 = CTkImage(img8_aula4,size=(1000,700))
            img9_aula4 = Image.open("imgs/aula4/slide-8.jpg")
            aula4img9 = CTkImage(img9_aula4,size=(1000,700))
            img10_aula4 = Image.open("imgs/aula4/slide-9.jpg")
            aula4img10 = CTkImage(img10_aula4,size=(1000,700))
            img11_aula4 = Image.open("imgs/aula4/slide-10.jpg")
            aula4img11 = CTkImage(img11_aula4,size=(1000,700))
            img12_aula4 = Image.open("imgs/aula4/fim.jpg")
            aula4img12 = CTkImage(img12_aula4,size=(1000,700))
            btsair = Image.open("imgs/saida_click.png")
            btsairimg = CTkImage(btsair, size=(25,25))
            aula4.state("icon")
            frameaulas = CTkScrollableFrame(aula4,width= 1000, height= 700)
            frameaulas.grid(rowspan = 18, columnspan = 5,column =25, pady = 10, padx = (150,220),sticky="e")
            Labelaula1 = CTkLabel(frameaulas,image=aula4img1,text="")
            Labelaula1.grid()
            Labelaula2 = CTkLabel(frameaulas,image=aula4img2,text="")
            Labelaula2.grid()
            Labelaula3 = CTkLabel(frameaulas,image=aula4img3,text="")
            Labelaula3.grid()
            Labelaula4 = CTkLabel(frameaulas,image=aula4img4,text="")
            Labelaula4.grid()
            Labelaula5 = CTkLabel(frameaulas,image=aula4img5,text="")
            Labelaula5.grid()
            Labelaula6 = CTkLabel(frameaulas,image=aula4img6,text="")
            Labelaula6.grid()
            Labelaula7 = CTkLabel(frameaulas,image=aula4img7,text="")
            Labelaula7.grid()
            Labelaula8 = CTkLabel(frameaulas,image=aula4img8,text="")
            Labelaula8.grid()
            Labelaula9 = CTkLabel(frameaulas,image=aula4img9,text="")
            Labelaula9.grid()
            Labelaula10 = CTkLabel(frameaulas,image=aula4img10,text="")
            Labelaula10.grid()
            Labelaula11 = CTkLabel(frameaulas,image=aula4img11,text="")
            Labelaula11.grid()
            btnsair = customtkinter.CTkButton(aula4,image=btsairimg,text="sair",command=sairInfra)
            btnsair.grid(row=4,column=0,sticky="s",pady=(0,10))  
            aula4.mainloop()
        def aula5Ciber():
            def sairciber():
                telmenu.state("zoomed")
                aula5.destroy()
            telmenu.state("icon")
            paginas = 0
            aula5 = ctk.CTkToplevel()
            aula5.state("zoomed")
            aula5.configure(fg_color = "#ffad2d")
            img1_aula5 = Image.open("imgs/aula5/ciber-capa.jpg")
            aula5img1 = CTkImage(img1_aula5,size=(1000,700))
            img2_aula5 = Image.open("imgs/aula5/slide-2.jpg")
            aula5img2 = CTkImage(img2_aula5,size=(1000,700))
            img3_aula5 = Image.open("imgs/aula5/slide-3.jpeg")
            aula5img3 = CTkImage(img3_aula5,size=(1000,700))
            img4_aula5 = Image.open("imgs/aula5/slide-4.jpg")
            aula5img4 = CTkImage(img4_aula5,size=(1000,700))
            img5_aula5 = Image.open("imgs/aula5/slide-5.jpg")
            aula5img5 = CTkImage(img5_aula5,size=(1000,700))
            img6_aula5 = Image.open("imgs/aula5/slide-6.jpg")
            aula5img6 = CTkImage(img6_aula5,size=(1000,700))
            img7_aula5 = Image.open("imgs/aula5/slide-7.jpg")
            aula5img7 = CTkImage(img7_aula5,size=(1000,700))
            img8_aula5 = Image.open("imgs/aula5/slide-8.jpg")
            aula5img8 = CTkImage(img8_aula5,size=(1000,700))
            img9_aula5 = Image.open("imgs/aula5/slide-9.jpg")
            aula5img9 = CTkImage(img9_aula5,size=(1000,700))
            img10_aula5 = Image.open("imgs/aula5/slide-10.jpg")
            aula5img10 = CTkImage(img10_aula5,size=(1000,700))
            img11_aula5 = Image.open("imgs/aula5/slide-11.jpg")
            aula5img11 = CTkImage(img11_aula5,size=(1000,700))
            img12_aula5 = Image.open("imgs/aula5/fim.jpg")
            aula5img12 = CTkImage(img12_aula5,size=(1000,700))
            btsair = Image.open("imgs/saida_click.png")
            btsairimg = CTkImage(btsair, size=(25,25))
            aula5.state("icon")
            frameaulas = CTkScrollableFrame(aula5,width= 1000, height= 700)
            frameaulas.grid(rowspan = 18, columnspan = 5,column =25, pady = 10, padx = (150,220),sticky="e")
            Labelaula1 = CTkLabel(frameaulas,image=aula5img1,text="")
            Labelaula1.grid()
            Labelaula2 = CTkLabel(frameaulas,image=aula5img2,text="")
            Labelaula2.grid()
            Labelaula3 = CTkLabel(frameaulas,image=aula5img3,text="")
            Labelaula3.grid()
            Labelaula4 = CTkLabel(frameaulas,image=aula5img4,text="")
            Labelaula4.grid()
            Labelaula5 = CTkLabel(frameaulas,image=aula5img5,text="")
            Labelaula5.grid()
            Labelaula6 = CTkLabel(frameaulas,image=aula5img6,text="")
            Labelaula6.grid()
            Labelaula7 = CTkLabel(frameaulas,image=aula5img7,text="")
            Labelaula7.grid()
            Labelaula8 = CTkLabel(frameaulas,image=aula5img8,text="")
            Labelaula8.grid()
            Labelaula9 = CTkLabel(frameaulas,image=aula5img9,text="")
            Labelaula9.grid()
            Labelaula10 = CTkLabel(frameaulas,image=aula5img10,text="")
            Labelaula10.grid()
            Labelaula11 = CTkLabel(frameaulas,image=aula5img11,text="")
            Labelaula11.grid()
            Labelaula12 = CTkLabel(frameaulas,image=aula5img12,text="")
            Labelaula12.grid()
            btnsair = customtkinter.CTkButton(aula5,image=btsairimg,text="sair",command=sairciber)
            btnsair.grid(row=4,column=0,sticky="s",pady=(0,10))  
            aula5.mainloop()
            
        
        telmenu = ctk.CTk()
        telmenu.config(background="#ffad2d")
        aula = 0
        #Perguntar para a professora sobre a fonte desse código abaixo
        imgtelmenu = Image.open("imgs/menu.png")
        imgmenu = CTkImage(imgtelmenu,size=(90,33))
        telmenu.after(0,lambda: telmenu.wm_state("zoomed"))
        framemenu1 = customtkinter.CTkFrame(telmenu,corner_radius=6, fg_color="#000075", bg_color="#ffad2d")
        framemenu1.grid(pady=0,padx=(0,0),column=0,columnspan=4, row = 0,sticky="wn")
        btnmenu = customtkinter.CTkButton(framemenu1,image=imgmenu,text="",command=expansao,height=25, width=30,font=("arial",15), fg_color="#000075")
        frameaulas = customtkinter.CTkFrame(telmenu,height=500, width=100,corner_radius=6, fg_color="#000075", bg_color="#ffad2d")
        frameaulas.grid(pady = (0,10),padx = (0,0),column=9, row = 0, rowspan=30, sticky = "ne")
        frameaulas.grid_anchor("e")
        btnmenu.grid(row=1, padx=(0,10))
        btnmenu.grid_anchor(anchor="e")
        lblPython = customtkinter.CTkLabel(frameaulas, text="Aulas Python", font=("Calibri", 22))
        lblPython.grid(padx = 0, pady=(10,25),column = 1, row = 0)
        btnaula1 = customtkinter.CTkButton(frameaulas,text="AULA 1", font=("arial", 15),command=aula1Python)
        btnaula1.grid(padx = 0,pady = 0,row= 1, column= 1)
        btnaula2 = customtkinter.CTkButton(frameaulas,text="AULA 2", command=aula2Python, font=("arial", 15))
        btnaula2.grid(padx = 0,pady = 0,row= 2, column= 1)
        btnaula3 = customtkinter.CTkButton(frameaulas,text="AULA 3",command=aula3Python, font=("arial", 15))
        btnaula3.grid(padx = 0,pady = 0,row= 3, column= 1)
        lblInfra = customtkinter.CTkLabel(frameaulas, text="Aulas Infraestrutura", font=("Calibri", 22))
        lblInfra.grid(padx = 25, pady=(10,25),column = 2, row = 0)
        btnaula1infra = customtkinter.CTkButton(frameaulas,text="AULA 1", font=("arial", 15),command=aula4Infra)
        btnaula1infra.grid(padx = 0,pady = 0,row= 1, column= 2)
        lblCyber = customtkinter.CTkLabel(frameaulas, text="Aulas Cibersegurança", font=("Calibri", 22))
        lblCyber.grid(padx = 25, pady=(10,25),column = 3, row = 0)
        btnaula1Cyber = customtkinter.CTkButton(frameaulas,text="AULA 1", font=("arial", 15),command=aula5Ciber)
        btnaula1Cyber.grid(padx = 0,pady = 0,row= 1, column= 3)


        #btnatvPy1 = customtkinter.CTkButton(frameaulas,text="ATIVDADE 1 Python", font=("arial", 15),command=py1atv)
        #btnatvPy1.grid(padx = 0,pady = 10,row= 5, column= 1)
        #btnatvPy2 = customtkinter.CTkButton(frameaulas,text="ATIVDADE 2 Python", font=("arial", 15),command=py2atv)
        #btnatvPy2.grid(padx = 0,pady = 10,row= 6, column= 1 )
        btnatvPy3 = customtkinter.CTkButton(frameaulas,text="ATIVDADE Complementar Python", font=("arial", 15),command=py3atv)
        btnatvPy3.grid(padx = 0,pady = 10,row= 7, column= 1)
        telmenu.mainloop()


    else:
        errotell = ctk.CTkToplevel(tellinicial)
        errotell.title("LOGIN OU SENHA INVALIDOS")
        errotell.geometry("600x400")
        fundoerro = customtkinter.CTkImage(Imagemerro,size=(600,400))
        labelfundo2 = customtkinter.CTkLabel(errotell, text="",image=fundoerro )
        labelfundo2.place(x=0, y=0, relwidth=1, relheight=1)  # Ajusta ao tamanho da janela
        #messagebox.showinfo("Atenção","Usuario ou Senha Invalidos")
        errotell.mainloop()

#Tela Inicial
tellinicial = ctk.CTk()
tellinicial.title("Pythoco Aprendiagem")
tellinicial.state("zoomed")
tellinicial.geometry("1024x920")
Imagemerro = Image.open("imgs/loginerro.png")
#fundotellerro = customtkinter.CTkImage(Imagemerro, size=(600,400))
Imagem = Image.open("imgs/LOGIN.png")
fundo = customtkinter.CTkImage(Imagem, size= (1370, 720))
tellinicial.configure(image_bg = fundo)
labelfundo = customtkinter.CTkLabel(tellinicial, text="",image=fundo )
labelfundo.place(x=0, y=0, relwidth=1, relheight=1)  # Ajusta ao tamanho da janela

frame_palavras = ctk.CTkFrame(tellinicial,height=500, width=400, corner_radius= 5, fg_color= "#000075", bg_color="#000075")

text1 = customtkinter.CTkLabel(frame_palavras, text="Informe o seu Usuario:", font=("Arial", 30), text_color="White")

entrada_login = CTkEntry(frame_palavras, bg_color="#000075",fg_color="white", height=30,border_width=0,font=("Arial", 22),text_color="Black")  # Campo de entrada para o primeiro valor

text2 = customtkinter.CTkLabel(frame_palavras, text="Informe a Senha:", font=("Arial", 30), text_color="White")

entrada_senha = CTkEntry(frame_palavras, bg_color="#000075",fg_color="white", height=30,border_width=0,font=("Arial", 22),text_color="Black")  # Campo de entrada para o primeiro valor

btnlogin = customtkinter.CTkButton(frame_palavras, text="Fazer Login",anchor="center",corner_radius=5, command=Logar,height=80, width= 240,font=("Arial", 22),text_color="White")

#Posicionamento dos elementos
text1.grid(row=1,pady=3,padx=(35,0))
entrada_login.grid(row=2, padx=60, pady=20,sticky="ew")
text2.grid(row=3,pady=(30,20))
entrada_senha.grid(row=4, padx=60, pady=20, sticky="ew")
btnlogin.grid(row=5,pady=30,padx=60)
frame_palavras.grid(pady=100, padx=120)
tellinicial.state("icon")
tellinicial.mainloop()

