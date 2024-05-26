import pygame

# Inicializar Pygame
pygame.init()

# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Definir las dimensiones de la pantalla
ANCHO = 700
ALTO = 500

# Definir la velocidad de la pelota y las paletas
velocidad_pelota = [3, 3]
velocidad_paleta = 0

# Definir la clase de la paleta
class Paleta(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def mover(self, y):
        self.rect.y += y

# Definir la clase de la pelota
class Pelota(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = ANCHO // 2
        self.rect.y = ALTO // 2

    def reiniciar(self):
        self.rect.x = ANCHO // 2
        self.rect.y = ALTO // 2

# Crear la pantalla del juego
pantalla = pygame.display.set_mode([ANCHO, ALTO])
pygame.display.set_caption("Pong")

# Crear las paletas
paleta_jugador = Paleta(BLANCO, 10, 100)
paleta_jugador.rect.x = 20
paleta_jugador.rect.y = ALTO // 2 - 50

paleta_oponente = Paleta(BLANCO, 10, 100)
paleta_oponente.rect.x = ANCHO - 30
paleta_oponente.rect.y = ALTO // 2 - 50

# Crear la pelota
pelota = Pelota(BLANCO, 10, 10)

# Crear todos los sprites
todos_los_sprites = pygame.sprite.Group()
todos_los_sprites.add(paleta_jugador, paleta_oponente, pelota)

# Bucle principal del juego
jugando = True
reloj = pygame.time.Clock()

while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                velocidad_paleta = -5
            elif evento.key == pygame.K_DOWN:
                velocidad_paleta = 5
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                velocidad_paleta = 0

    # Movimiento de la paleta del jugador
    paleta_jugador.mover(velocidad_paleta)

    # Movimiento de la paleta del oponente
    paleta_oponente.rect.y = pelota.rect.y

    # Movimiento de la pelota
    pelota.rect.x += velocidad_pelota[0]
    pelota.rect.y += velocidad_pelota[1]

    # Comprobar colisiones con las paletas
    if pygame.sprite.collide_rect(pelota, paleta_jugador) or pygame.sprite.collide_rect(pelota, paleta_oponente):
        velocidad_pelota[0] *= -1

    # Comprobar si la pelota sale de la pantalla
    if pelota.rect.x >= ANCHO or pelota.rect.x <= 0:
        velocidad_pelota[0] *= -1
    if pelota.rect.y >= ALTO or pelota.rect.y <= 0:
        velocidad_pelota[1] *= -1

    # Limpiar la pantalla
    pantalla.fill(NEGRO)

    # Dibujar todos los sprites
    todos_los_sprites.draw(pantalla)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad de actualización
    reloj.tick(60)

pygame.quit()