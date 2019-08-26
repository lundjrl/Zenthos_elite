from bullet import Bullet
from alien import Alien
from time import sleep
import sys
import pygame


def check_events(ai_settings, screen, stats, play_button, ship,
        swarm, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship,
                    swarm, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, play_button, ship, swarm,
        bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        pygame.mouse.set_visible(False)

        # Reset game stats.
        stats.reset_stats()
        stats.game_active = True
        
        # Empty the list of aliens and bullets.
        swarm.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, swarm)
        ship.center_ship()


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, stats, ship, swarm, bullets,
        play_button):
    """Update images on the screen and flip to the new screen."""
    screen.fill(ai_settings.bg_color)
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet() 
    ship.blitme()
    swarm.draw(screen)
    
    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()
    # Make the most recently drawn screen visible.
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, swarm, bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    check_bullet_alien_collisions(ai_settings, screen, ship, swarm, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, swarm, bullets):
    """Respond to bullet-alien collisions then remove both."""
    collisions = pygame.sprite.groupcollide(bullets, swarm, True, True)

    if len(swarm) == 0:
        # Destroy existing bullets and repopulate fleet.
        bullets.empty()
        create_fleet(ai_settings, screen, ship, swarm)


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_on_screen:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_size_swarm_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row.""" 
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width)) 
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height - 
            (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, swarm, alien_num, row_num):
    """Create an alien and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_num
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_num
    swarm.add(alien)


def create_fleet(ai_settings, screen, ship, swarm):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_size_swarm_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
            alien.rect.height)

    # First row of the swarm
    for row_num in range(number_rows):
        for alien_num in range(number_aliens_x):
            create_alien(ai_settings, screen, swarm, alien_num, row_num)


def update_aliens(ai_settings, stats, screen, ship, swarm, bullets):
    """Update the positions of all aliens in the fleet."""
    check_fleet_edges(ai_settings, swarm)
    swarm.update()
    check_aliens_bottom(ai_settings, stats, screen, ship, swarm, bullets)


def check_fleet_edges(ai_settings, swarm):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in swarm.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, swarm)
            break


def change_fleet_direction(ai_settings, swarm):
    """Drop the fleet and change direction."""
    for alien in swarm.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, swarm, bullets):
    """Respond to ship being hit by alien."""
    if stats.ships_left > 0:
        # Decrease number of ships.
        stats.ships_left -= 1

        # Empty the list of aliens and bullets.
        swarm.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, swarm)
        ship.center_ship()

        # Pause...
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, screen, ship, swarm, bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in swarm.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, swarm, bullets)
            break

