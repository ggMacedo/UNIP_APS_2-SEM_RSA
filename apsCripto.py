#CHAVE PÚBLICA: 684

i = 0;
frase = "";
desCript = False;

tamanho_chave = 32;
p = 23;
q = 29;
n = p * q;
phi_n = (p - 1) * (q - 1);
e = 17;

print("Bem-vindo ao encriptador RSA!");
while(i == 0):

    print("\n(1) Criptografar frase\n (2) Descriptografar frase\n (3) Mostrar frase\n (4) Sair\n");
    
    try:
        op= int(input("Digite a opção desejada: "));
    except:
        print("Valor inválido!");
    else:
            
        if(op == 1):# Criptografar

            chavPublc = n + e;

            chav = int(input("Digite a chave pública de acesso para criptografar: "));

            if(chav == chavPublc):
                
                frase = input("Digite a frase que será criptografada: ");

                cifra = "";
                
                for c in frase:
                    letra_asc = ord(c);
                    cifra += str(pow(letra_asc, e, n)) + ' ';

                desCript = False;
                                  
            else:
                print("Chave incorreta! Acesso negado.");
                
        elif(op == 2):# Descriptografar

            if(frase != ""):

                s = 0;
                antigo_s = 1;
                t = 1;
                antigo_t = 0;
                r = phi_n;
                antigo_r = e;

                while r != 0:
                    quociente = antigo_r // r;
                    antigo_r, r = r, antigo_r - quociente * r;
                    antigo_s, s = s, antigo_s - quociente * s;
                    antigo_t, t = t, antigo_t - quociente * t;
                            

                mdc = antigo_r;
                x = antigo_s;
                y = antigo_t;

                if x < 0:
                    x += n;

                d = x;

                chavPriv = p + q + d;

                if(chavPriv == 197):
                    
                    print("Chave correta!");

                    frase = "";
              
                    partes = cifra.split();
                    for parte in partes:
                        if parte:
                            c = int(parte);
                            frase+= chr(pow(c, d, n));
             
                    desCript = True;
                    print("Frase descriptografada com sucesso!!");
                                           
                else:
                    print("Chave incorreta! Acesso negado.");
                
            else:
                 print("Não existe frase criptografada ainda!");

        elif(op == 3): # Mostrar frases

            if(frase != ""):
           
                if(desCript == True):
                    print("Frase descriptografada: ", frase);
                elif(desCript == False):
                    print("Frase criptografada: ", cifra);

            else:
                print("Não existe frase ainda!");
                           
        elif(op == 4): # Sair
            
            print("Obrigado por utilizar o sistema!");
            break;
        
        else:
            print("Opção inválida!");
