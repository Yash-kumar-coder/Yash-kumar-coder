import re
import os

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

custom_ascii = """                             ====---                                  
                         ==+#%#%%%%%%%%**+=-                            
                    -+=*####%%%%%@@%%@@%%%%#*+                          
                  ==##+##%#%%@@@@@@@%%@@@@@@%%+=                        
                 =*+###%%%@@@@@@@@%%%@@@@@@@@@#*                        
                -+%%%%%@@@@%%%%%%%%%%@@@@@@@@%#*                        
                -+#%@@@%@%#######%%%%%@@@@@@@%#=                        
                 -*######+---==+**########%%@#=                         
                 +#####*+-::-==+*#*****#%###%-                          
                 -*###+-::-+++########%%####++=                         
                  =*#++====#==+#%%*+**%#####+++                         
                   =**+-:.::=-=**+-+:=*###**+=                          
                   =--::::.::-====-::-+*##***=                          
                  :=+*-:::::::-=++-+++##**+++=                          
                   :---:-:::::-----=*####**++-                          
                     ::=-::::::-##++*###%%*++                           
                        =--:::-==-=+###****+-                           
                         :-==-------+*****+-                            
                         :::-+++===*#%###*-                             
                          :::::-+#%%%%%%##+                             
                          :::::-=*########*+++*+                        
                        -*::::::=*###****####%@@@%#+=                   
                    -=**#-:::::-=+********#%@@@@@@@@@@%#*+              
                 =+#######=:::--=+*++*##%@@@@@@@@@@@@@@@@@%%#+          
             =*#%%%%#%%%%%%#**+***##%%%%%%%%%%%%@@@@@@@@@@@@@@%%=       
          +*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@%=        
        *%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@*          
      +%%%%%%%@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%=           
     -#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@%%#=      
       -#@@@%%%%%%%%%%@%%%%%@@@%%%%%%%%%%%%%%%%%%%%%%@@*-               
          +#%%%%%%%%%%@%%%%@@@@%%%%@@%%%%%%%%%%%%%%%#+                  
             =*%%%%%%@@@%%@@@@@%%%@@@%%%%%%%%%%%%*=                     
                 =+#%@@@%@@@@@@%%%@@@%%%%@%%#+=                         
                       =++**########**+=="""

def update_svg(filepath, ascii_art):
    content = read_file(filepath)
    
    # Revert height back to 530px for a more balanced design
    content = re.sub(r'height="750px"', 'height="530px"', content)
    
    # Trim leading spaces (min 5 spaces based on our test)
    lines = ascii_art.split('\n')
    min_leading_spaces = min(len(line) - len(line.lstrip()) for line in lines if line.strip())
    trimmed_lines = [line[min_leading_spaces:] for line in lines]
    
    fill_color = "#24292f" if "light" in filepath else "#c9d1d9"
    # Added font-size="9px" to make the wide ASCII art fit on the left side
    ascii_block = f'<text x="15" y="30" fill="{fill_color}" class="ascii" font-size="9px">\n'
    y = 40
    for line in trimmed_lines:
        ascii_block += f'<tspan x="15" y="{y}">{line}</tspan>\n'
        y += 13 # smaller line height to match smaller font
    ascii_block += '</text>'
    
    content = re.sub(r'<text x="15" y="30" fill=".*?" class="ascii".*?>.*?</text>', ascii_block, content, flags=re.DOTALL)
    write_file(filepath, content)

if __name__ == "__main__":
    print(f"Applying design fixes...")
    update_svg('c:\\Users\\Admin\\Desktop\\Yash-kumar-coder\\light_mode.svg', custom_ascii)
    update_svg('c:\\Users\\Admin\\Desktop\\Yash-kumar-coder\\dark_mode.svg', custom_ascii)
