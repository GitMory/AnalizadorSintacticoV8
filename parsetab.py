
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BREAK DIVIDE DO ELSE EQ EQUALS FALSE FLOAT GE GT ID IF INT LBRACE LBRACKET LE LPAREN LT MINUS NE NOT NUM OR PLUS RBRACE RBRACKET REAL RPAREN SEMICOLON TIMES TRUE WHILEprograma : bloquebloque : LBRACE decls instrs RBRACEdecls : decls decl\n             | emptydecl : tipo ID SEMICOLONtipo : tipo LBRACKET NUM RBRACKET\n            | basicobasico : INT\n                | FLOATinstrs : instrs stmt\n              | emptyinstr : loc EQUALS bool SEMICOLON\n             | IF LPAREN bool RPAREN instr\n             | IF LPAREN bool RPAREN instr ELSE instr\n             | WHILE LPAREN bool RPAREN instr\n             | DO instr WHILE LPAREN bool RPAREN SEMICOLON\n             | BREAK SEMICOLON\n             | bloqueloc : loc LBRACKET bool RBRACKET\n           | IDbool : bool OR comb\n            | combcomb : comb AND igualdad\n            | igualdadigualdad : igualdad EQ rel\n                | igualdad NE rel\n                | relrel : expr LT expr\n           | expr LE expr\n           | expr GE expr\n           | expr GT expr\n           | exprexpr : expr PLUS term\n            | expr MINUS term\n            | termterm : term TIMES unario\n            | term DIVIDE unario\n            | unariounario : NOT unario\n              | MINUS unario\n              | factorfactor : LPAREN bool RPAREN\n              | loc\n              | NUM\n              | REAL\n              | TRUE\n              | FALSEstmt : loc EQUALS bool SEMICOLON\n            | IF LPAREN bool RPAREN instr\n            | IF LPAREN bool RPAREN instr ELSE instr\n            | WHILE LPAREN bool RPAREN instr\n            | DO instr WHILE LPAREN bool RPAREN SEMICOLON\n            | BREAK SEMICOLON\n            | bloqueempty :'
    
_lr_action_items = {'LBRACE':([0,3,4,5,6,7,8,13,14,18,20,28,34,35,36,62,64,81,82,101,102,105,106,107,108,111,112,113,115,116,117,118,],[3,-55,-55,-4,3,-3,-11,-2,-10,3,-54,3,-18,-53,-5,-17,-48,3,3,-49,-51,3,-12,3,3,-15,-13,-50,-52,3,-16,-14,]),'$end':([1,2,13,],[0,-1,-2,]),'INT':([3,4,5,7,36,],[-55,11,-4,-3,-5,]),'FLOAT':([3,4,5,7,36,],[-55,12,-4,-3,-5,]),'RBRACE':([3,4,5,6,7,8,13,14,20,34,35,36,62,64,101,102,106,111,112,113,115,117,118,],[-55,-55,-4,13,-3,-11,-2,-10,-54,-18,-53,-5,-17,-48,-49,-51,-12,-15,-13,-50,-52,-16,-14,]),'IF':([3,4,5,6,7,8,13,14,18,20,28,34,35,36,62,64,81,82,101,102,105,106,107,108,111,112,113,115,116,117,118,],[-55,-55,-4,16,-3,-11,-2,-10,32,-54,32,-18,-53,-5,-17,-48,32,32,-49,-51,32,-12,32,32,-15,-13,-50,-52,32,-16,-14,]),'WHILE':([3,4,5,6,7,8,13,14,18,20,28,29,34,35,36,57,62,64,81,82,101,102,105,106,107,108,111,112,113,115,116,117,118,],[-55,-55,-4,17,-3,-11,-2,-10,30,-54,30,58,-18,-53,-5,83,-17,-48,30,30,-49,-51,30,-12,30,30,-15,-13,-50,-52,30,-16,-14,]),'DO':([3,4,5,6,7,8,13,14,18,20,28,34,35,36,62,64,81,82,101,102,105,106,107,108,111,112,113,115,116,117,118,],[-55,-55,-4,18,-3,-11,-2,-10,28,-54,28,-18,-53,-5,-17,-48,28,28,-49,-51,28,-12,28,28,-15,-13,-50,-52,28,-16,-14,]),'BREAK':([3,4,5,6,7,8,13,14,18,20,28,34,35,36,62,64,81,82,101,102,105,106,107,108,111,112,113,115,116,117,118,],[-55,-55,-4,19,-3,-11,-2,-10,33,-54,33,-18,-53,-5,-17,-48,33,33,-49,-51,33,-12,33,33,-15,-13,-50,-52,33,-16,-14,]),'ID':([3,4,5,6,7,8,9,10,11,12,13,14,18,20,24,25,26,27,28,34,35,36,45,47,49,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,81,82,84,101,102,103,105,106,107,108,111,112,113,115,116,117,118,],[-55,-55,-4,21,-3,-11,22,-7,-8,-9,-2,-10,21,-54,21,21,21,21,21,-18,-53,-5,21,21,21,21,21,21,-17,-6,-48,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-49,-51,21,21,-12,21,21,-15,-13,-50,-52,21,-16,-14,]),'LBRACKET':([9,10,11,12,15,21,31,38,63,80,],[23,-7,-8,-9,25,-20,25,25,-6,-19,]),'ELSE':([13,34,62,101,106,111,112,117,118,],[-2,-18,-17,108,-12,-15,116,-16,-14,]),'EQUALS':([15,21,31,80,],[24,-20,60,-19,]),'LPAREN':([16,17,24,25,26,27,30,32,45,47,49,58,59,60,61,65,66,67,68,69,70,71,72,73,74,75,76,83,84,103,],[26,27,49,49,49,49,59,61,49,49,49,84,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,103,49,49,]),'SEMICOLON':([19,21,22,33,38,39,40,41,42,43,44,46,48,50,51,52,53,77,78,80,86,88,89,90,91,92,93,94,95,96,97,98,99,100,110,114,],[35,-20,36,62,-43,64,-22,-24,-27,-32,-35,-38,-41,-44,-45,-46,-47,-40,-39,-19,106,-21,-23,-25,-26,-28,-29,-30,-31,-33,-34,-36,-37,-42,115,117,]),'TIMES':([21,38,44,46,48,50,51,52,53,77,78,80,96,97,98,99,100,],[-20,-43,75,-38,-41,-44,-45,-46,-47,-40,-39,-19,75,75,-36,-37,-42,]),'DIVIDE':([21,38,44,46,48,50,51,52,53,77,78,80,96,97,98,99,100,],[-20,-43,76,-38,-41,-44,-45,-46,-47,-40,-39,-19,76,76,-36,-37,-42,]),'LT':([21,38,43,44,46,48,50,51,52,53,77,78,80,96,97,98,99,100,],[-20,-43,69,-35,-38,-41,-44,-45,-46,-47,-40,-39,-19,-33,-34,-36,-37,-42,]),'LE':([21,38,43,44,46,48,50,51,52,53,77,78,80,96,97,98,99,100,],[-20,-43,70,-35,-38,-41,-44,-45,-46,-47,-40,-39,-19,-33,-34,-36,-37,-42,]),'GE':([21,38,43,44,46,48,50,51,52,53,77,78,80,96,97,98,99,100,],[-20,-43,71,-35,-38,-41,-44,-45,-46,-47,-40,-39,-19,-33,-34,-36,-37,-42,]),'GT':([21,38,43,44,46,48,50,51,52,53,77,78,80,96,97,98,99,100,],[-20,-43,72,-35,-38,-41,-44,-45,-46,-47,-40,-39,-19,-33,-34,-36,-37,-42,]),'PLUS':([21,38,43,44,46,48,50,51,52,53,77,78,80,92,93,94,95,96,97,98,99,100,],[-20,-43,73,-35,-38,-41,-44,-45,-46,-47,-40,-39,-19,73,73,73,73,-33,-34,-36,-37,-42,]),'MINUS':([21,24,25,26,27,38,43,44,45,46,47,48,49,50,51,52,53,59,60,61,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,84,92,93,94,95,96,97,98,99,100,103,],[-20,45,45,45,45,-43,74,-35,45,-38,45,-41,45,-44,-45,-46,-47,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-40,-39,-19,45,74,74,74,74,-33,-34,-36,-37,-42,45,]),'EQ':([21,38,41,42,43,44,46,48,50,51,52,53,77,78,80,89,90,91,92,93,94,95,96,97,98,99,100,],[-20,-43,67,-27,-32,-35,-38,-41,-44,-45,-46,-47,-40,-39,-19,67,-25,-26,-28,-29,-30,-31,-33,-34,-36,-37,-42,]),'NE':([21,38,41,42,43,44,46,48,50,51,52,53,77,78,80,89,90,91,92,93,94,95,96,97,98,99,100,],[-20,-43,68,-27,-32,-35,-38,-41,-44,-45,-46,-47,-40,-39,-19,68,-25,-26,-28,-29,-30,-31,-33,-34,-36,-37,-42,]),'AND':([21,38,40,41,42,43,44,46,48,50,51,52,53,77,78,80,88,89,90,91,92,93,94,95,96,97,98,99,100,],[-20,-43,66,-24,-27,-32,-35,-38,-41,-44,-45,-46,-47,-40,-39,-19,66,-23,-25,-26,-28,-29,-30,-31,-33,-34,-36,-37,-42,]),'OR':([21,38,39,40,41,42,43,44,46,48,50,51,52,53,54,55,56,77,78,79,80,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,104,109,],[-20,-43,65,-22,-24,-27,-32,-35,-38,-41,-44,-45,-46,-47,65,65,65,-40,-39,65,-19,65,65,65,-21,-23,-25,-26,-28,-29,-30,-31,-33,-34,-36,-37,-42,65,65,]),'RBRACKET':([21,37,38,40,41,42,43,44,46,48,50,51,52,53,54,77,78,80,88,89,90,91,92,93,94,95,96,97,98,99,100,],[-20,63,-43,-22,-24,-27,-32,-35,-38,-41,-44,-45,-46,-47,80,-40,-39,-19,-21,-23,-25,-26,-28,-29,-30,-31,-33,-34,-36,-37,-42,]),'RPAREN':([21,38,40,41,42,43,44,46,48,50,51,52,53,55,56,77,78,79,80,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,104,109,],[-20,-43,-22,-24,-27,-32,-35,-38,-41,-44,-45,-46,-47,81,82,-40,-39,100,-19,105,107,-21,-23,-25,-26,-28,-29,-30,-31,-33,-34,-36,-37,-42,110,114,]),'NUM':([23,24,25,26,27,45,47,49,59,60,61,65,66,67,68,69,70,71,72,73,74,75,76,84,103,],[37,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,]),'NOT':([24,25,26,27,45,47,49,59,60,61,65,66,67,68,69,70,71,72,73,74,75,76,84,103,],[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,]),'REAL':([24,25,26,27,45,47,49,59,60,61,65,66,67,68,69,70,71,72,73,74,75,76,84,103,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'TRUE':([24,25,26,27,45,47,49,59,60,61,65,66,67,68,69,70,71,72,73,74,75,76,84,103,],[52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,]),'FALSE':([24,25,26,27,45,47,49,59,60,61,65,66,67,68,69,70,71,72,73,74,75,76,84,103,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'bloque':([0,6,18,28,81,82,105,107,108,116,],[2,20,34,34,34,34,34,34,34,34,]),'decls':([3,],[4,]),'empty':([3,4,],[5,8,]),'instrs':([4,],[6,]),'decl':([4,],[7,]),'tipo':([4,],[9,]),'basico':([4,],[10,]),'stmt':([6,],[14,]),'loc':([6,18,24,25,26,27,28,45,47,49,59,60,61,65,66,67,68,69,70,71,72,73,74,75,76,81,82,84,103,105,107,108,116,],[15,31,38,38,38,38,31,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,31,31,38,38,31,31,31,31,]),'instr':([18,28,81,82,105,107,108,116,],[29,57,101,102,111,112,113,118,]),'bool':([24,25,26,27,49,59,60,61,84,103,],[39,54,55,56,79,85,86,87,104,109,]),'comb':([24,25,26,27,49,59,60,61,65,84,103,],[40,40,40,40,40,40,40,40,88,40,40,]),'igualdad':([24,25,26,27,49,59,60,61,65,66,84,103,],[41,41,41,41,41,41,41,41,41,89,41,41,]),'rel':([24,25,26,27,49,59,60,61,65,66,67,68,84,103,],[42,42,42,42,42,42,42,42,42,42,90,91,42,42,]),'expr':([24,25,26,27,49,59,60,61,65,66,67,68,69,70,71,72,84,103,],[43,43,43,43,43,43,43,43,43,43,43,43,92,93,94,95,43,43,]),'term':([24,25,26,27,49,59,60,61,65,66,67,68,69,70,71,72,73,74,84,103,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,96,97,44,44,]),'unario':([24,25,26,27,45,47,49,59,60,61,65,66,67,68,69,70,71,72,73,74,75,76,84,103,],[46,46,46,46,77,78,46,46,46,46,46,46,46,46,46,46,46,46,46,46,98,99,46,46,]),'factor':([24,25,26,27,45,47,49,59,60,61,65,66,67,68,69,70,71,72,73,74,75,76,84,103,],[48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> bloque','programa',1,'p_programa','analizador.py',91),
  ('bloque -> LBRACE decls instrs RBRACE','bloque',4,'p_bloque','analizador.py',94),
  ('decls -> decls decl','decls',2,'p_decls','analizador.py',97),
  ('decls -> empty','decls',1,'p_decls','analizador.py',98),
  ('decl -> tipo ID SEMICOLON','decl',3,'p_decl','analizador.py',101),
  ('tipo -> tipo LBRACKET NUM RBRACKET','tipo',4,'p_tipo','analizador.py',104),
  ('tipo -> basico','tipo',1,'p_tipo','analizador.py',105),
  ('basico -> INT','basico',1,'p_basico','analizador.py',108),
  ('basico -> FLOAT','basico',1,'p_basico','analizador.py',109),
  ('instrs -> instrs stmt','instrs',2,'p_instrs','analizador.py',112),
  ('instrs -> empty','instrs',1,'p_instrs','analizador.py',113),
  ('instr -> loc EQUALS bool SEMICOLON','instr',4,'p_instr','analizador.py',116),
  ('instr -> IF LPAREN bool RPAREN instr','instr',5,'p_instr','analizador.py',117),
  ('instr -> IF LPAREN bool RPAREN instr ELSE instr','instr',7,'p_instr','analizador.py',118),
  ('instr -> WHILE LPAREN bool RPAREN instr','instr',5,'p_instr','analizador.py',119),
  ('instr -> DO instr WHILE LPAREN bool RPAREN SEMICOLON','instr',7,'p_instr','analizador.py',120),
  ('instr -> BREAK SEMICOLON','instr',2,'p_instr','analizador.py',121),
  ('instr -> bloque','instr',1,'p_instr','analizador.py',122),
  ('loc -> loc LBRACKET bool RBRACKET','loc',4,'p_loc','analizador.py',125),
  ('loc -> ID','loc',1,'p_loc','analizador.py',126),
  ('bool -> bool OR comb','bool',3,'p_bool','analizador.py',129),
  ('bool -> comb','bool',1,'p_bool','analizador.py',130),
  ('comb -> comb AND igualdad','comb',3,'p_comb','analizador.py',133),
  ('comb -> igualdad','comb',1,'p_comb','analizador.py',134),
  ('igualdad -> igualdad EQ rel','igualdad',3,'p_igualdad','analizador.py',137),
  ('igualdad -> igualdad NE rel','igualdad',3,'p_igualdad','analizador.py',138),
  ('igualdad -> rel','igualdad',1,'p_igualdad','analizador.py',139),
  ('rel -> expr LT expr','rel',3,'p_rel','analizador.py',142),
  ('rel -> expr LE expr','rel',3,'p_rel','analizador.py',143),
  ('rel -> expr GE expr','rel',3,'p_rel','analizador.py',144),
  ('rel -> expr GT expr','rel',3,'p_rel','analizador.py',145),
  ('rel -> expr','rel',1,'p_rel','analizador.py',146),
  ('expr -> expr PLUS term','expr',3,'p_expr','analizador.py',149),
  ('expr -> expr MINUS term','expr',3,'p_expr','analizador.py',150),
  ('expr -> term','expr',1,'p_expr','analizador.py',151),
  ('term -> term TIMES unario','term',3,'p_term','analizador.py',154),
  ('term -> term DIVIDE unario','term',3,'p_term','analizador.py',155),
  ('term -> unario','term',1,'p_term','analizador.py',156),
  ('unario -> NOT unario','unario',2,'p_unario','analizador.py',159),
  ('unario -> MINUS unario','unario',2,'p_unario','analizador.py',160),
  ('unario -> factor','unario',1,'p_unario','analizador.py',161),
  ('factor -> LPAREN bool RPAREN','factor',3,'p_factor','analizador.py',164),
  ('factor -> loc','factor',1,'p_factor','analizador.py',165),
  ('factor -> NUM','factor',1,'p_factor','analizador.py',166),
  ('factor -> REAL','factor',1,'p_factor','analizador.py',167),
  ('factor -> TRUE','factor',1,'p_factor','analizador.py',168),
  ('factor -> FALSE','factor',1,'p_factor','analizador.py',169),
  ('stmt -> loc EQUALS bool SEMICOLON','stmt',4,'p_stmt','analizador.py',172),
  ('stmt -> IF LPAREN bool RPAREN instr','stmt',5,'p_stmt','analizador.py',173),
  ('stmt -> IF LPAREN bool RPAREN instr ELSE instr','stmt',7,'p_stmt','analizador.py',174),
  ('stmt -> WHILE LPAREN bool RPAREN instr','stmt',5,'p_stmt','analizador.py',175),
  ('stmt -> DO instr WHILE LPAREN bool RPAREN SEMICOLON','stmt',7,'p_stmt','analizador.py',176),
  ('stmt -> BREAK SEMICOLON','stmt',2,'p_stmt','analizador.py',177),
  ('stmt -> bloque','stmt',1,'p_stmt','analizador.py',178),
  ('empty -> <empty>','empty',0,'p_empty','analizador.py',181),
]
