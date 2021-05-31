"""
Our beloved robot friend Karel has turned into a virtual pet, which you can feed, play games with, and put to bed. Can you keep Karel alive?
"""
import pygame, random

# screen
WIDTH = 800
HEIGHT = 600

# setting Karel's basic stats
HAPPINESS = 50
HUNGER = 0
ENERGY = 100

# setting all the moods Karel can have
UNHAPPY = 40
DEADFROMNOTPLAYING = 0
HUNGRY = 30
DEADFROMNOTEATING = 100
SLEEPY = 50
DEADFROMNOTSLEEPING = 0 

def call_karel(screen, petImg, x, y):
    screen.blit(petImg, (x, y))

def call_happiness_stats(screen, happiness_text, x, y, happiness_stat_bar):
    screen.blit(happiness_text, (x, y))
    screen.blit(happiness_stat_bar, (x, y + 50))

def call_hunger_stats(screen, hunger_text, x, y, hunger_stat_bar):
    screen.blit(hunger_text, (x, y))
    screen.blit(hunger_stat_bar, (x, y + 50))

def call_energy_stats(screen, energy_text, x, y, energy_stat_bar):
    screen.blit(energy_text, (x, y))
    screen.blit(energy_stat_bar, (x, y + 50))

def call_instructions(screen, instructions, x, y):
    screen.blit(instructions, (x, y))

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # create title and icon
    pygame.display.set_caption("PyPet Karel")
    icon = pygame.image.load('karel.png')
    pygame.display.set_icon(icon)

    # game starts with neutral Karel, with basic stats
    petImg = neutral_karel = pygame.image.load('neutral_karel.png')
    happy_karel = pygame.image.load('happy_karel.png')
    sleepy_karel = pygame.image.load('sleepy_karel.png') 
    hungry_karel = pygame.image.load('hungry_karel.png')
    dead_karel = pygame.image.load('dead_karel.png')
    unhappy_karel = pygame.image.load('unhappy_karel.png')

    petX = 300
    petY = 200
    petX_change = 3
    petY_change = 0

    # create stats bars
    happiness_text = pygame.image.load('happiness_bar.png')
    happinessX = 25
    happinessY = 0

    hunger_text = pygame.image.load('hunger_bar.png')
    hungerX = happinessX + 250
    hungerY = 0

    energy_text = pygame.image.load('energy_bar.png')
    energyX = hungerX + 250
    energyY = 0

    hunger_stat_bar = empty_bar = pygame.image.load('empty_bar.png')
    bar_10 = pygame.image.load('10_bar.png')
    bar_20 = pygame.image.load('20_bar.png')
    bar_30 = pygame.image.load('30_bar.png')
    bar_40 = pygame.image.load('40_bar.png')
    happiness_stat_bar = bar_50 = pygame.image.load('50_bar.png')
    bar_60 = pygame.image.load('60_bar.png')
    bar_70 = pygame.image.load('70_bar.png')
    bar_80 = pygame.image.load('80_bar.png')
    bar_90 =pygame.image.load('90_bar.png')
    energy_stat_bar = full_bar = pygame.image.load('full_bar.png')
    
    # create instructions bar
    instructions = pygame.image.load('key_instructions.png')
    instructionsX = 0
    instructionsY = 550
    
    # intializing Karel's stats
    karel_happiness = HAPPINESS
    karel_hunger = HUNGER
    karel_energy =  ENERGY

    # game loop
    running = True
    update_stats_elapsed = 0
    while running:
        elapsed_milliseconds = clock.tick(40)
        update_stats_elapsed += elapsed_milliseconds

        # Create background color
        screen.fill((255, 255, 255))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # player can alter stats by feeding, playing or putting Karel to bed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    food = random.randint(1, 10)
                    karel_hunger = max(0, karel_hunger - food)
                if event.key == pygame.K_p:
                    play = random.randint(1, 10)
                    karel_happiness = min(100, karel_happiness + play)
                if event.key == pygame.K_s:
                    sleep = random.randint(1, 10)
                    karel_energy = min(100, karel_energy + sleep)

        # update Karel's stats randomly, every 5 seconds
        if update_stats_elapsed >= 5000:
            happiness_update = random.randint(1, 8)
            karel_happiness = max(0, karel_happiness - happiness_update)
            hunger_update = random.randint(1, 8)
            karel_hunger = min(100, karel_hunger + hunger_update)
            energy_update = random.randint(1, 8)
            karel_energy = min(100, karel_energy - energy_update)
            update_stats_elapsed = 0
          
        # change Karel images when happy, hungry, sleepy or sleeping
        # dead Karel
        if (
            (karel_happiness <= DEADFROMNOTPLAYING) 
            or (karel_hunger >= DEADFROMNOTEATING) 
            or (karel_energy <= DEADFROMNOTSLEEPING)
        ):
            petImg = dead_karel
        # neutral Karel
        elif (karel_happiness == HAPPINESS) and (karel_hunger < HUNGRY) and (karel_energy > SLEEPY):
            petImg = neutral_karel
        # happy Karel
        elif (karel_happiness > HAPPINESS) and (karel_hunger < HUNGRY) and (karel_energy > SLEEPY):
            petImg = happy_karel
        # unhappy Karel
        elif (karel_happiness < HAPPINESS):
            petImg = unhappy_karel
        # hungry Karel
        elif karel_hunger >= HUNGRY:
            petImg = hungry_karel
        # sleepy Karel
        elif karel_energy <= SLEEPY:
            petImg = sleepy_karel

        # update display happiness stats
        if karel_happiness == 100:
            happiness_stat_bar = full_bar 
        if (karel_happiness >= 90) and (karel_happiness < 100):
            happiness_stat_bar = bar_90
        if (karel_happiness >= 80) and (karel_happiness < 90):
            happiness_stat_bar = bar_80
        if (karel_happiness >= 70) and (karel_happiness < 80):
            happiness_stat_bar = bar_70
        if (karel_happiness >= 60) and (karel_happiness < 70):
            happiness_stat_bar = bar_60
        if (karel_happiness >= 50) and (karel_happiness < 60):
            happiness_stat_bar = bar_50
        if (karel_happiness >= 40) and (karel_happiness < 50):
            happiness_stat_bar = bar_40
        if (karel_happiness >= 30) and (karel_happiness < 40):
            happiness_stat_bar = bar_30
        if (karel_happiness >= 20) and (karel_happiness < 30):
            happiness_stat_bar = bar_20
        if (karel_happiness >= 10) and (karel_happiness < 20):
            happiness_stat_bar = bar_10
        if (karel_happiness >= 0) and (karel_happiness < 10):
            happiness_stat_bar = empty_bar

        # update display hunger stats
        if karel_hunger == 100:
            hunger_stat_bar = full_bar
        if (karel_hunger >= 90) and (karel_hunger < 100):
            hunger_stat_bar = bar_90
        if (karel_hunger >= 80) and (karel_hunger < 90):
            hunger_stat_bar = bar_80
        if (karel_hunger >= 70) and (karel_hunger < 80):
            hunger_stat_bar = bar_70
        if (karel_hunger >= 60) and (karel_hunger < 70):
            hunger_stat_bar = bar_60
        if (karel_hunger >= 50) and (karel_hunger < 60):
            hunger_stat_bar = bar_50
        if (karel_hunger >= 40) and (karel_hunger < 50):
            hunger_stat_bar = bar_40
        if (karel_hunger >= 30) and (karel_hunger < 40):
            hunger_stat_bar = bar_30
        if (karel_hunger >= 20) and (karel_hunger < 30):
            hunger_stat_bar = bar_20
        if (karel_hunger >= 10) and (karel_hunger < 20):
            hunger_stat_bar = bar_10
        if (karel_hunger >= 0) and (karel_hunger < 10):
            hunger_stat_bar = empty_bar

        # update display energy stats
        if karel_energy == 100:
            energy_stat_bar = full_bar
        if (karel_energy >= 90) and (karel_energy < 100):
            energy_stat_bar = bar_90
        if (karel_energy >= 80) and (karel_energy < 90):
            energy_stat_bar = bar_80
        if (karel_energy >= 70) and (karel_energy < 80):
            energy_stat_bar = bar_70
        if (karel_energy >= 60) and (karel_energy < 70):
            energy_stat_bar = bar_60
        if (karel_energy >= 50) and (karel_energy < 60):
            energy_stat_bar = bar_50
        if (karel_energy >= 40) and (karel_energy < 50):
            energy_stat_bar = bar_40
        if (karel_energy >= 30) and (karel_energy < 40):
            energy_stat_bar = bar_30
        if (karel_energy >= 20) and (karel_energy < 30):
            energy_stat_bar = bar_20
        if (karel_energy >= 10) and (karel_energy < 20):
            energy_stat_bar = bar_10
        if (karel_energy >= 0) and (karel_energy < 10):
            energy_stat_bar = empty_bar

        # karel moves around the screen, within the boundaries
        petX += petX_change
        if petX <= 0:
            petX = 0
            petX_change = random.randint(0, 5)
            petY_change = random.randint(-5, 5)
        elif petX >= 600:
            petX = 600
            petX_change = -random.randint(0, 5)
            petY_change = random.randint(-5, 5)

        petY += petY_change
        if petY <= 100:
            petY = 100
            petX_change = random.randint(-5, 5)
            petY_change = random.randint(0, 5)
        elif petY >= 350:
            petY = 350
            petX_change = random.randint(-5, 5)
            petY_change = -random.randint(0,5)
     
        # call Karel
        call_karel(screen, petImg, petX, petY)

        # call stats
        call_happiness_stats(screen, happiness_text, happinessX, happinessY, happiness_stat_bar)
        call_hunger_stats(screen, hunger_text, hungerX, hungerY, hunger_stat_bar)
        call_energy_stats(screen, energy_text, energyX, energyY, energy_stat_bar)

        # display key instructions
        call_instructions(screen, instructions, instructionsX, instructionsY)
    
        pygame.display.update()

if __name__ == '__main__':
    main()