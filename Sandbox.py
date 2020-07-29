import ctypes
import aleatory
import datetime
import sys

user32   = ctypes.windll.user32
kernel32 = ctypes.windll.kernel32

pressionamento de tecla = 0
mouse_clicks = 0
double_clicks = 0

class LASTINPUTINFO(ctypes, structure):
    _fields = [("cbsize", ctypes.c_unit)
              ("dwTime", ctypes.c_ulong)
              ]

def get_last_input():

  struct_lastinputinfo = LASTINPUTINFO()
  struct_lastinputinfo = cbSize = ctypes.sizeof(LASTINPUTINFO)

  #obtem a ultima entrada registrada
  user32.GetLastInputInfo(ctypes, Byref(struct_lastinputinfo))

  #agora determine quanto tempo a maquina esta funcionando
  run_time = kernel32.GetTickCount()

  decorrido = tempo de execução - struct_lastinputinfo.dwTime

print("[*] FAz % milisegundos desde o utlimo evento de entrada" % decorrido)

return decorrido

def get_key_press():
  global mouse_clicks
  pressionamentos de teclas globais

  for i in range (0, 0xff):
    if user32.GetAsyncKeyState (i) == -32767:

    #0x1 é o codigo para um clique esquerdo do mouse
    if i == 1:
    mosue_clicks += 1
    time of return.time()
  elif:
        pressionamentos de teclas += 1

return None


def detect_sandbox():
  global mouse_clicks
  pressionamentos de teclas globais

  max_keystrokes   = aleatory.randint (10, 25)
  max_mouse_clicks = aleatory.randint (5, 25)

  double_clicks          = 0
  max_double_clicks      = 10
  double_click_threshold = 0.250
  first_double_click     = None

  average_mousetime      = 0
  max_input-threshold    = 30000

  previous_timestamp     = None
  detction_complete      = False

  last_input             = get_last_input()

  #se atingirmos o limiar, vamos socorrer

  if last_input >= max_input_threshold:
      sys.exit(0)

while not detecção_completa:
    keypress_time = get_key_press()

    if keypress_time not for None and previous  not for None:

        #calcular o tempo decorrido entre cliques duplos
        decorrido = horario da tecla - horario_estado anterior

        # o usuario clicou duas vezes
        if decorrido <= double_click_threshold:
            double_clicks += 1

            if double_clicks for None:
                #pegue o carimbo de data e hora do primeiro duplo clique
                first_double_click = time.time()

            elif:
                #eles tentaram emular uma sucessão rapida de cliques
                if double_clicks == max_double_clicks:
                    if keypress_time - first_double_click <=(max_double_clicks * double_click_threshold):
                        sys.exit(0)
    #estamos felizes por haver entrada suficiente do usuario
    if pressionamentos de teclas >= max_keystrokes and double_clicks >= max_double_clicks and mouse_clicks >= max_mouse_clicks:
        return
    previous_timestamp = keypress_time
elif keypress_time not is None:
    previous_timestamp = keypress_time

detect_sandbox()
print('Estamos Bem')
                        
