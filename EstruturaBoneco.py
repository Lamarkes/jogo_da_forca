# Estrutura do boneco utilizado no joguinho
vazio = """
            """

forca = """       
  ___________
  |         !  
  |             
  |
  |
  |
  |
-----
"""

cabeca = """
   ___________
  |          !  
  |         o>o    
  |          - 
  |
  |
  |
----- """

corpo = """ 
   ___________
  |          !  
  |         o>o    
  |          - 
  |          |
  |          |
  |
----- """


braco_esquerdo = """ 
   ___________
  |          !  
  |         o>o    
  |          - 
  |         /|
  |          |
  |
-----"""

braco_direito = """ 
   ___________
  |          !  
  |         o>o    
  |          - 
  |         /|\\
  |          |
  |            
-----"""


perna_esquerda = """ 
   ___________
  |          !  
  |         o>o    
  |          - 
  |         /|\\
  |          |
  |         / 
----- """


perna_direita = """ 
   ___________
  |          !  
  |         x>x    
  |          - 
  |         /|\\
  |          |
  |         / \\
----- """

estrutura_boneco = [vazio,
                    cabeca,
                    corpo,
                    braco_esquerdo,
                    braco_direito,
                    perna_esquerda,
                    perna_direita,
                    ]


