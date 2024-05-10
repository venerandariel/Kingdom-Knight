import pygame
import sys
import time
import os

# Pygame'i başlat
pygame.init()

# Ekran boyutu
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 680

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Karakterin animasyon resimlerinin dizini
ANIMATION_FOLDER = "images"
SOUNDTRACK_FOLDER = "soundtrack"

# Oyuncu sınıfı
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = [pygame.image.load(os.path.join(ANIMATION_FOLDER, f"right_run_{i+1}.png")).convert_alpha() for i in range(8)]
        self.images = [pygame.transform.scale(image, (100, 100)) for image in self.images]  # Boyutunu büyüt
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.4)
        self.direction = 'right'  # Başlangıçta karakterin sağa baktığını varsayalım
        self.move_right = False
        #idle
        self.image_idle = pygame.image.load("Idle.png").convert_alpha()
        self.image = self.image_idle
        self.image = pygame.transform.scale(self.image_idle, (60,120))
        


        

    def update(self):
        # Tuşa basılıysa animasyonu oynatma
        if self.move_right:
            self.index += 0.5
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[int(self.index)]
        else:
            self.image = self.image_idle
            self.image = pygame.transform.scale(self.image_idle, (60,120))


# Pencere oluşturma
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Kingdom Knight")

# Oyuncu oluşturma
player = Player()  # Kullanmak istediğiniz görüntünün dosya yolunu girin

# Oyuncu grubu oluşturma
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Müzik yükleme
pygame.mixer.music.load(os.path.join(SOUNDTRACK_FOLDER,"deadcells.mp3"))
pygame.mixer.music.play(-1)  # -1 döngü yapar, yani müzik bitene kadar çalar

# Arkaplan
background_image = pygame.image.load(os.path.join(ANIMATION_FOLDER,"castle.png"))
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))


# Oyun döngüsü
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.move_right = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player.move_right = False
         
    # Oyuncuyu güncelleme
    player.update()

    # Ekranı temizleme
    screen.fill(BLACK)

     # Arka plan resmini çizme
    screen.blit(background_image, (0, 0))

    # Tüm sprite'ları çizme
    all_sprites.draw(screen)

    # Ekranı güncelleme
    pygame.display.flip()

    # Oyun döngüsünü sınırlandırma
    clock.tick(15)  # FPS değerini ayarlayabilirsiniz

# Pygame'i kapat
pygame.quit()
sys.exit()
