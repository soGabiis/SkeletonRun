from code.entity import Entity
from code.enemy import Enemy
from code.player import Player
from code.playerSword import PlayerShot

class entityMediator:

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for ent in entity_list:

            # PlayerShot Enemy Collision
            if isinstance(ent, PlayerShot):
                for target in entity_list:
                    if ent == target:
                        continue
                    if isinstance(target, Enemy):
                        offset_x = target.rect.left - ent.rect.left
                        offset_y = target.rect.top - ent.rect.top

                        if ent.mask and target.mask:
                            if ent.mask.overlap(target.mask, (offset_x, offset_y)):
                                target.health -= 1
                                ent.health = 0

            # Enemy colliding with Player
            elif isinstance(ent, Enemy):
                for target in entity_list:
                    if ent == target:
                        continue
                    if isinstance(target, Player):

                        if not ent.rect.colliderect(target.rect):
                            continue

                        offset_x = target.rect.left - ent.rect.left
                        offset_y = target.rect.top - ent.rect.top

                        # check pixel-perfect with mask
                        if ent.mask and target.mask:
                            if ent.mask.overlap(target.mask, (offset_x, offset_y)):
                                if not target.invulnerable:
                                    target.health -= 1
                                    target.invulnerable = True
                                    target.invulnerable_timer = 30
                                    print(f"[DEBUG] Player levou dano. health = {target.health}")

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        to_remove = []

        for ent in entity_list:
            if hasattr(ent, 'health') and ent.health <= 0:
                # Only removes the Player if he is not dying (end animation)
                if isinstance(ent, Player):
                    if not getattr(ent, "is_dying", False):
                        to_remove.append(ent)
                else:
                    to_remove.append(ent)

        for ent in to_remove:
            entity_list.remove(ent)
