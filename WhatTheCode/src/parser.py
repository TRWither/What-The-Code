import ply.yacc as yacc
from lexer import tokens
import os

def exe_bendew(p):
    while True:
        print("wedneb")
        
def exe_shesh(p):
    for i in range(1, 101):
        folder_name = f'folder{i}'
        os.makedirs(folder_name)
        
def exe_suuu(p):
    while True:
        print("SUUUUUUUUUUU")
        
def exe_help(p):
    print("""
          Hey ! Is it your first time on WhatTheCode ?
          If yes, you are in the right place !
          
          So listen me : there are docs on GitHub I wrote
          myself, OK ? Go read it.
          
          And remember : listen the potato.
          """)

def p_statement(p):
    '''statement : expression ENDINSTR
                 | print ENDINSTR
                 | zigoto ENDINSTR
                 | bendew ENDINSTR
                 | what_is_it ENDINSTR
                 | shesh ENDINSTR
                 | yes ENDINSTR
                 | im_a_hacker ENDINSTR
                 | suuu ENDINSTR
                 | help ENDINSTR
                 | license ENDINSTR
                 | i_hate_this_lang ENDINSTR'''
    p[0] = p[1]

def p_expression(p):
    '''expression : expression PLS_ADD expression
                  | expression PLS_SUB expression
                  | expression IM_BATMAN expression
                  | expression YAY expression
                  | NUM'''
    if len(p) == 4:
        if p[2] == 'pls_add':
            p[0] = p[1] + p[3]
        elif p[2] == 'pls_sub':
            p[0] = p[1] - p[3]
        elif p[2] == 'i_am_batman':
            p[0] = p[1] * p[3]
        elif p[2] == 'yay':
            if p[3] != 0:
                p[0] = p[1] / p[3]
            else:
                print("YAY by 0 ? Impossible !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        p[0] = p[1]
        
def p_print(p):
    '''print : BRO_SAY STR'''
    p[0] = p[2]
    
def p_zigoto(p):
    '''zigoto : ZIGOTO'''
    p[0] = """
    

.___/\                 ___.                  __           __                                       .__        
|   )/_____   _____    \_ |__ _____    _____|  | __ _____/  |_  ______   ____   ____    ____  __ __|__| ____  
|   |/     \  \__  \    | __ \\__  \  /  ___/  |/ // __ \   __\ \____ \_/ __ \ /    \  / ___\|  |  \  |/    \ 
|   |  Y Y  \  / __ \_  | \_\ \/ __ \_\___ \|    <\  ___/|  |   |  |_> >  ___/|   |  \/ /_/  >  |  /  |   |  \
|___|__|_|  / (____  /  |___  (____  /____  >__|_ \\___  >__|   |   __/ \___  >___|  /\___  /|____/|__|___|  /
          \/       \/       \/     \/     \/     \/    \/       |__|        \/     \//_____/               \/ 


    """
    
def p_bendew(p):
    '''bendew : BENDEW'''
    p[0] = exe_bendew(p)
    
def p_what_is_it(p):
    '''what_is_it : WHAT_IS_IT'''
    p[0] = print("That's something. -_-")
    
def p_shesh(p):
    '''shesh : SHEEEEEEEESH'''
    p[0] = exe_shesh(p)
    
def p_yes(p):
    '''yes : YES'''
    p[0] = print("No")
    
def p_im_a_hacker(p):
    '''im_a_hacker : IM_A_HACKER'''
    p[0] = print("You : What's a computer ?\nThe Potato : SUUUUUUUUUU")
    
def p_suuu(p):
    '''suuu : SUUUUUUUUUUU'''
    p[0] = exe_suuu(p)
    
def p_help(p):
    '''help : HELP'''
    p[0] = exe_help(p)
    
def p_license(p):
    '''license : LICENSE'''
    p[0] = print('''
                 MIT License

Copyright (c) 2024 Wither__

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

                 ''')
    
def p_i_hate_this_lang(p):
    '''i_hate_this_lang : I_HATE_THIS_LANG'''
    p[0] = print('''
                 You will regret what you said...
                 Remember :
                 The potato is watching you.
                 ''')
            
def p_error(p):
    print("LMAO SYNTAX ERROR LOOOOOOOOSEEEER")

parser = yacc.yacc(debug=True)
