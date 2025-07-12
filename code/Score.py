import pygame
import os

from code.Const import WIN_WIDTH, WIN_HEIGHT


class Score:
    def __init__(self, window):
        self.window = window
        self.bg = pygame.image.load('./asset/Battleground1.png').convert_alpha()
        self.font = pygame.font.SysFont("Lucida Sans Typewriter", 40)
        self.big_font = pygame.font.SysFont("Lucida Sans Typewriter", 60)

    def save_score(self, score: int, name: str):
        with open("score.txt", "a") as f:
            f.write(f"{name},{score}\n")

    def show_score(self):
        pygame.mixer_music.load('./asset/814964__josefpres__piano-loops-132-efect-4-octave-long-loop-120-bpm.wav')
        pygame.mixer_music.play(-1)

        scores = []
        if os.path.exists("score.txt"):
            with open("score.txt", "r") as f:
                for line in f:
                    try:
                        name, value = line.strip().split(",")
                        scores.append((name, int(value)))
                    except:
                        continue

        # Sort and get the 10 best
        scores = sorted(scores, key=lambda x: x[1], reverse=True)[:10]

        waiting = True
        while waiting:
            self.window.fill((0, 0, 0))
            self.window.blit(self.bg, (0, 0))

            title = self.big_font.render("TOP 10 Melhores Scores", True, (255, 255, 0))
            self.window.blit(title, (800, 50))

            for idx, (name, score) in enumerate(scores):
                text = self.font.render(f"{idx+1:2}. {name:<12}- {score}", True, (255, 255, 255))
                self.window.blit(text, (100, 150 + idx * 45))

            back_text = self.font.render("Pressione ESC para voltar", True, (255, 100, 100))
            self.window.blit(back_text, (1500, WIN_HEIGHT - 75))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    waiting = False
