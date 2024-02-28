.486
JUMPS
STAY SEGMENT STACK 'STACK'
      db 100h dup(?)
STAY ENDS
ASSUME CS:CODE
      include d:\macro.zbr
CODE SEGMENT use16
            file db 'font.fnt',0
            amount dd 0
            result dw ?
            align 4
            scroll db '                    ',255
                   db '                    ',255
                   db '                    ',255
                   db '                    ',255
                   db '   What am I        ',255
                   db '                    ',255
                   db '   drawing?         ',255
                   db '                    ',255
                   db '  kxctf{...._U      ',255
                   db '                    ',255
                   db '  n0_D0$_m0d3_      ',255
                   db '                    ',255
                   db '  w4s_en4bl3d}      ',255
                   db '                    ',255
                   db '   ( 0 _ 0 )        ',255
                   db '                    ',255
                   db '                    ',255,0
            align 4
            line dw 1
            align 4
            line2 dw 1
            align 4
            color db 255
            align 4
            finished db 0
Start:
      cld
      call load_font
      call clear_buffer
      mov ax,0013h          
      int 10h
      call set_palette
      xor ax,0a000h
      mov es,ax
      call time
      mov cs:[time1],eax
main:
      call sparks
      call show
      call draw
      call drawing
      call _fire
      inc cs:[amount]
      mov ah,cs:[finished]
      cmp ah,0
      jz main
      call time
      mov cs:[time2],eax
      mov ax,0003h
      int 10h
      mov eax,cs:[amount]
      mov ebx,cs:[time2]
      sub ebx,cs:[time1]
      call fps
      mov ax,4c00h
      int 21h
_fire proc
      mov di,320
      mov cx,203*320
fire:
      call smoke
      mov es:[di-320],dl
      inc di
      dec cx
jnz fire
      ret
smoke:
      xor ax,ax
      mov al,es:[di]
      mov dx,ax
      mov al,es:[di+320]
      add dx,ax
      mov al,es:[di+321]
      add dx,ax
      mov al,es:[di+319]
      add dx,ax
      shr dx,2
skip_dec:
      cmp dl,0
      je  rys
      dec dl
rys:
      ret
_fire endp
sparks proc
      mov di,197*320
      mov cx,320
insert:
      call drawing
      mov es:[di],dl
      mov es:[di+320],dl
      mov es:[di+640],dl
      inc di
      dec cx
jnz  insert
      ret
drawing:
      mov ax,cs:[rand]
      mov dx,31413
      mul dx
      add ax,13849
      mov cs:[rand],ax
      mov dx,254
      mul dx
      ret
rand dw 12345
sparks endp
set_palette proc
      xor bl,bl
      xor bh,bh
      mov cx,64
set_red:
      mov dx,3c8h
      mov al,bl
      out dx,al
      inc dx
      mov al,bh
      out dx,al
      xor al,al
      out dx,al
      out dx,al
      inc bl
      inc bh
loop set_red
      mov bl,64
      xor bh,bh
      mov cx,64
set_green:
      mov dx,3c8h
      mov al,bl
      out dx,al
      inc dx
      mov al,63
      out dx,al
      mov al,bh
      out dx,al
      xor al,al
      out dx,al
      inc bl
      inc bh
loop set_green
      mov cx,63
      mov bl,128
      xor bh,bh
set_blue:
      mov dx,3c8h
      mov al,bl
      out dx,al
      inc dx
      mov al,63
      out dx,al
      mov al,63
      out dx,al
      mov al,bh
      out dx,al
      inc bl
      inc bh
loop set_blue
      mov cx,62
      mov bl,192
set_b:
      mov dx,3c8h
      mov al,bl
      out dx,al
      inc dx
      mov al,63
      out dx,al
      out dx,al
      out dx,al
      inc bl
loop set_b
      ret
set_palette endp
draw proc
      mov ax,seg FONT
      mov ds,ax
      lea si,font_buf
      mov bx,cs:[line2]
      lea bp,[scroll+bx]
      mov di,33600
scrolling:
      xor bx,bx
      mov bl,cs:[bp]
      cmp bl,255
      jz end_of_line
      cmp bl,0
      jz end_of_scroll
      sub bx,20h
      shl bx,5
      mov ax,cs:[line]
      shl ax,1
      add bx,ax 
      mov ax,ds:[si+bx]
      xchg ah,al
      mov cx,16
      mov dx,1000000000000000b
pixel:
      test ax,dx
      jz skip_put
      call put_pixel
skip_put:
      inc di
      shr dx,1
      dec cx
jnz  pixel
      inc bp
jmp  scrolling 
end_of_line:
      inc cs:[line]
      cmp cs:[line],15
      jna exit
      add cs:[line2],21
      mov cs:[line],0
exit:
      ret
end_of_scroll:
      mov cs:[line2],0
      mov cs:[finished],1
      jmp exit

put_pixel:
      mov bl,cs:[color]
      mov es:[di],bl
      ret
draw endp
show proc
      ret
show endp
move proc
      mov ax,0a000h
      mov ds,ax
      mov si,320
      xor di, di
      mov cx,4000 
      rep movsd
      ret
move endp
clear_buffer proc
      mov ax,0a000h
      mov es,ax
      xor di,di
      xor ax,ax
      mov cx,16000
      rep stosd
      ret
clear_buffer endp
load_font proc
      mov ah,3dh
      xor al,al
      push cs
      pop ds 
      lea dx,file
      int 21h
      mov bx,ax
      mov ax,seg FONT
      mov ds,ax
      lea dx,font_buf
      mov ah,3fh 
      mov cx,3072
      int 21h
      mov ah,3eh
      int 21h
      ret
load_font endp
include time.asm
CODE ENDS
FONT SEGMENT use16
     font_buf  db 3072 dup (?)
FONT ENDS
END Start