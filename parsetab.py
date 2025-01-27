
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABRIR ADICIONAR ALINHAR COLORIR CONTAINER CRIAR FECHAR ITEMS JUSTIFICAR NUMERO PARA STRING TAMANHO TELA TEXTO X comandos : comando\n                | comandos comando  comando : CRIAR TELA NUMERO X NUMERO comando : ADICIONAR TEXTO STRING comando : COLORIR TEXTO STRING PARA STRING  comando : ABRIR CONTAINER STRING NUMERO X NUMERO comando : FECHAR CONTAINER  comando : ALINHAR ITEMS CONTAINER STRING STRING  comando : JUSTIFICAR ITEMS CONTAINER STRING STRING comando : COLORIR CONTAINER STRING PARA STRING '
    
_lr_action_items = {'CRIAR':([0,1,2,10,16,20,32,33,34,36,37,38,],[3,3,-1,-2,-7,-4,-3,-5,-10,-8,-9,-6,]),'ADICIONAR':([0,1,2,10,16,20,32,33,34,36,37,38,],[4,4,-1,-2,-7,-4,-3,-5,-10,-8,-9,-6,]),'COLORIR':([0,1,2,10,16,20,32,33,34,36,37,38,],[5,5,-1,-2,-7,-4,-3,-5,-10,-8,-9,-6,]),'ABRIR':([0,1,2,10,16,20,32,33,34,36,37,38,],[6,6,-1,-2,-7,-4,-3,-5,-10,-8,-9,-6,]),'FECHAR':([0,1,2,10,16,20,32,33,34,36,37,38,],[7,7,-1,-2,-7,-4,-3,-5,-10,-8,-9,-6,]),'ALINHAR':([0,1,2,10,16,20,32,33,34,36,37,38,],[8,8,-1,-2,-7,-4,-3,-5,-10,-8,-9,-6,]),'JUSTIFICAR':([0,1,2,10,16,20,32,33,34,36,37,38,],[9,9,-1,-2,-7,-4,-3,-5,-10,-8,-9,-6,]),'$end':([1,2,10,16,20,32,33,34,36,37,38,],[0,-1,-2,-7,-4,-3,-5,-10,-8,-9,-6,]),'TELA':([3,],[11,]),'TEXTO':([4,5,],[12,13,]),'CONTAINER':([5,6,7,17,18,],[14,15,16,24,25,]),'ITEMS':([8,9,],[17,18,]),'NUMERO':([11,23,26,35,],[19,29,32,38,]),'STRING':([12,13,14,15,24,25,27,28,30,31,],[20,21,22,23,30,31,33,34,36,37,]),'X':([19,29,],[26,35,]),'PARA':([21,22,],[27,28,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'comandos':([0,],[1,]),'comando':([0,1,],[2,10,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> comandos","S'",1,None,None,None),
  ('comandos -> comando','comandos',1,'p_comandos','comandos.py',9),
  ('comandos -> comandos comando','comandos',2,'p_comandos','comandos.py',10),
  ('comando -> CRIAR TELA NUMERO X NUMERO','comando',5,'p_comando_tela','comandos.py',14),
  ('comando -> ADICIONAR TEXTO STRING','comando',3,'p_comando_texto','comandos.py',24),
  ('comando -> COLORIR TEXTO STRING PARA STRING','comando',5,'p_comando_colorir_texto','comandos.py',32),
  ('comando -> ABRIR CONTAINER STRING NUMERO X NUMERO','comando',6,'p_comando_abrir_container','comandos.py',43),
  ('comando -> FECHAR CONTAINER','comando',2,'p_comando_fechar_container','comandos.py',52),
  ('comando -> ALINHAR ITEMS CONTAINER STRING STRING','comando',5,'p_alinhar_items_container','comandos.py',57),
  ('comando -> JUSTIFICAR ITEMS CONTAINER STRING STRING','comando',5,'p_justificar_items_container','comandos.py',68),
  ('comando -> COLORIR CONTAINER STRING PARA STRING','comando',5,'p_comando_colorir_container','comandos.py',78),
]
