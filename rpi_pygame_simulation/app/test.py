import sys, pygame
#import pygame.examples.aliens as xmpl # 	— 	play the full aliens example
#import pygame.examples.oldalien as xmpl # 	— 	play the original aliens example
#import pygame.examples.stars as xmpl # 	— 	run a simple starfield example
#import pygame.examples.chimp as xmpl # 	— 	hit the moving chimp
#import pygame.examples.moveit as xmpl # 	— 	display animated objects on the screen
import pygame.examples.fonty as xmpl # 	— 	run a font rendering example
import pygame.gfxdraw
#import pygame.examples.freetype_misc as xmpl # 	— 	run a FreeType rendering example
#import pygame.examples.vgrade as xmpl # 	— 	display a vertical gradient
#import pygame.examples.eventlist as xmpl # 	— 	display pygame events
#import pygame.examples.arraydemo as xmpl # 	— 	show various surfarray effects
#import pygame.examples.sound as xmpl # 	— 	load and play a sound
#import pygame.examples.sound_array_demos as xmpl # 	— 	play various sndarray effects
#import pygame.examples.liquid as xmpl # 	— 	display an animated liquid effect
#import pygame.examples.glcube as xmpl # 	— 	display an animated 3D cube using OpenGL
#import pygame.examples.scrap_clipboard as xmpl # 	— 	access the clipboard
#import pygame.examples.mask as xmpl # 	— 	display multiple images bounce off each other using collision detection
#import pygame.examples.testsprite as xmpl # 	— 	show lots of sprites moving around
#import pygame.examples.headless_no_windows_needed as xmpl # 	— 	write an image file that is smoothscaled copy of an input file
#import pygame.examples.fastevents as xmpl # 	— 	stress test the fastevents module
#import pygame.examples.overlay as xmpl # 	— 	play a .pgm video using overlays
#import pygame.examples.blend_fill as xmpl # 	— 	demonstrate the various surface.fill method blend options
#import pygame.examples.blit_blends as xmpl # 	— 	uses alternative additive fill to that of surface.fill
#import pygame.examples.cursors as xmpl # 	— 	display two different custom cursors
#import pygame.examples.pixelarray as xmpl # 	— 	display various pixelarray generated effects
#import pygame.examples.scaletest as xmpl # 	— 	interactively scale an image using smoothscale
#import pygame.examples.midi as xmpl # 	— 	run a midi example
#import pygame.examples.scroll as xmpl # 	— 	run a Surface.scroll example that shows a magnified image
#import pygame.examples.camera as xmpl # 	— 	display video captured live from an attached camera
#import pygame.examples.playmus as xmpl # 	— 	play an audio file


pygame.init()

width_offset = 200
height_offset = 200

map = pygame.image.load("FullSizeRender.jpeg")
map_size = map_width, map_height = map.get_width()//2, map.get_height()//2
size = width, height = map_size[0] + width_offset, map_size[1] + height_offset
map_size = width, height = map.get_width()//2, map.get_height()//2
map = pygame.transform.scale(map, (map_size[0],map_size[1]))


black = 100, 100, 100

screen = pygame.display.set_mode(size)
pygame.gfxdraw.hline(screen, 5, 300, 522, (255,255,255))

while 1:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
           sys.exit()
        if event.type == pygame.KEYUP and event.key == 27:
            pass
           #sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pass
           #sys.exit()
        if event.type == pygame.VIDEORESIZE:
           width = event.w
           height = event.h
           size = width, height
           map = pygame.transform.scale(map, (width,height))
           screen.blit(map,(width_offset,0))
           screen = pygame.display.set_mode(size)

    screen.fill(black)
    screen.blit(map,(0,0))
    pygame.display.flip()
    pygame.time.delay(10)
