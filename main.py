import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from logger import log_event
from circleshape import CircleShape
import sys

def main():
        pygame.init()
        print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")
        screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        clock = pygame.time.Clock()
        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()
        shots = pygame.sprite.Group()
        Shot.containers = (shots,updatable,drawable)
        Player.containers = (updatable,drawable)
        Asteroid.containers = (asteroids, updatable, drawable)
        AsteroidField.containers = (updatable,)
        asteroida = AsteroidField()
        player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
        dt: float = 0.0

        while True:
            log_state()
            dt = clock.tick(60) /1000
            updatable.update(dt)
            for x in asteroids:
                if x.collides_with(player):
                    log_event("player_hit")
                    print("Game over!")
                    sys.exit()
            for x in asteroids:
                for shot in shots:
                    if x.collides_with(shot):
                        log_event("asteroid_shot")
                        x.split()
                        shot.kill()
                                
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            screen.fill("black")
            for x in drawable:
                x.draw(screen)
            
            
            pygame.display.flip()
            



if __name__ == "__main__":
    main()

