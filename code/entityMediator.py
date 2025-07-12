from code.entity import Entity
from code.enemy import Enemy
from code.player import Player
from code.playerSword import PlayerShot


class entityMediator:

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for ent in entity_list:

            # Colisão PlayerShot -> Enemy
            if isinstance(ent, PlayerShot):
                for target in entity_list:
                    if isinstance(target, Enemy):
                        offset_x = target.rect.left - ent.rect.left
                        offset_y = target.rect.top - ent.rect.top

                        if ent.mask and target.mask:
                            if ent.mask.overlap(target.mask, (offset_x, offset_y)):
                                target.health -= 1
                                ent.health = 0  # Remove a espada após acertar

            # Colisão Enemy -> Player
            elif isinstance(ent, Enemy):
                for target in entity_list:
                    if isinstance(target, Player):
                        offset_x = target.rect.left - ent.rect.left
                        offset_y = target.rect.top - ent.rect.top

                        if ent.mask and target.mask:
                            if ent.mask.overlap(target.mask, (offset_x, offset_y)):
                                if not target.invulnerable:
                                    target.health -= 1
                                    target.invulnerable = True
                                    target.invulnerable_timer = 60  # 1 segundo de invulnerabilidade (60 frames)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        to_remove = []
        for ent in entity_list:
            if hasattr(ent, 'health') and ent.health <= 0:
                to_remove.append(ent)

        for ent in to_remove:
            entity_list.remove(ent)
