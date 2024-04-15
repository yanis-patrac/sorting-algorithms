import pygame
import random
import time
import math

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 800, 600
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
FPS = 60

# Couleurs prédéfinies
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Liste des algorithmes de tri
SORT_ALGORITHMS = {
    "Tri par sélection": lambda colors: sorted(colors, key=lambda c: sum(c)),
    "Tri à bulles": lambda colors: sorted(colors, key=lambda c: sum(c)),
    "Tri par insertion": lambda colors: sorted(colors, key=lambda c: sum(c)),
    "Tri rapide": lambda colors: sorted(colors, key=lambda c: sum(c)),
    "Tri aléatoire": lambda colors: random.sample(colors, len(colors))
}

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Sorting")

# Font pour le texte
font = pygame.font.Font(None, 36)

# Fonction pour trier les couleurs
def sort_colors(colors, algorithm):
    start_time = time.time()
    sorted_colors = SORT_ALGORITHMS[algorithm](colors[:])  # Utilisation d'une copie de la liste
    end_time = time.time()
    return sorted_colors, end_time - start_time

# Fonction pour afficher le texte
def draw_text(text, x, y):
    text_surface = font.render(text, True, WHITE)
    screen.blit(text_surface, (x, y))

# Fonction pour générer des couleurs aléatoires
def generate_random_colors(count):
    return [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(count)]

# Fonction pour afficher des boutons
def draw_button(text, rect, action=None):
    mouse_pos = pygame.mouse.get_pos()
    clicked = pygame.mouse.get_pressed()[0]
    button_color = WHITE if rect.collidepoint(mouse_pos) else BLACK
    pygame.draw.rect(screen, button_color, rect)
    draw_text(text, rect.x + 10, rect.y + 10)
    if action and rect.collidepoint(mouse_pos) and clicked:
        action()

# Fonction pour afficher des éléments de l'interface utilisateur
def draw_ui(algorithm, circle_count):
    draw_button("Nouvelles couleurs", pygame.Rect(20, HEIGHT - 150, 200, 50), generate_new_colors)
    draw_button("Démarrer le tri", pygame.Rect(230, HEIGHT - 150, 150, 50), lambda: start_sorting(algorithm))
    draw_text(f"Algorithme de tri: {algorithm}", 20, HEIGHT - 100)
    draw_text(f"Nombre de cercles: {circle_count}", 20, HEIGHT - 50)

# Fonction pour générer de nouvelles couleurs
def generate_new_colors():
    global colors
    global algorithm
    global circle_count
    circle_count = random.randint(20, 100)
    colors = generate_random_colors(circle_count)
    algorithm = random.choice(list(SORT_ALGORITHMS.keys()))

# Fonction pour démarrer le tri
def start_sorting(algorithm):
    global sorting
    sorting = True

# Fonction pour animer les cercles pendant le tri
def animate_circles(colors, sorted_colors):
    duration = 0.5  # Durée de l'animation en secondes
    start_time = time.time()
    while time.time() - start_time < duration:
        interpolation = (time.time() - start_time) / duration
        interpolated_colors = [(int(start_col[0] + (end_col[0] - start_col[0]) * interpolation),
                                int(start_col[1] + (end_col[1] - start_col[1]) * interpolation),
                                int(start_col[2] + (end_col[2] - start_col[2]) * interpolation))
                               for start_col, end_col in zip(colors, sorted_colors)]
        draw_circles(interpolated_colors)
        pygame.display.flip()
        pygame.time.wait(10)  # Attente de 10 ms pour limiter le taux de rafraîchissement

# Fonction pour afficher les cercles colorés
def draw_circles(colors):
    circle_radius = 100
    circle_count = len(colors)
    angle_step = 2 * math.pi / circle_count

    for i, color in enumerate(colors):
        angle = i * angle_step
        circle_x = CENTER_X + circle_radius * math.cos(angle)
        circle_y = CENTER_Y + circle_radius * math.sin(angle)
        pygame.draw.circle(screen, color, (int(circle_x), int(circle_y)), 10)

# Boucle principale
clock = pygame.time.Clock()
running = True
sorting = False
circle_count = random.randint(20, 100)
colors = generate_random_colors(circle_count)
algorithm = random.choice(list(SORT_ALGORITHMS.keys()))
while running:
    screen.fill(BLACK)  # Efface l'écran avec du noir

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not sorting:
            if event.button == 1:  # Clic gauche
                generate_new_colors()
            elif event.button == 3:  # Clic droit
                start_sorting(algorithm)

    # Affichage de l'interface utilisateur
    draw_ui(algorithm, len(colors))

    # Tri et animation des cercles
    if sorting:
        draw_text("Tri en cours...", 20, HEIGHT - 150)
        sorted_colors, sorting_time = sort_colors(colors, algorithm)
        animate_circles(colors, sorted_colors)
        draw_text(f"Temps de tri: {sorting_time:.4f} secondes", 20, HEIGHT - 100)
        sorting = False

    # Affichage des cercles colorés
    draw_circles(colors)

    pygame.display.flip()  # Met à jour l'affichage
    clock.tick(FPS)

# Fermeture de Pygame
pygame.quit()
