from code.entity import Entity
from code.enemy import Enemy
from code.playerSword import PlayerShot


class entityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for ent in entity_list:
            if isinstance(ent, PlayerShot):
                for target in entity_list:
                    if isinstance(target, Enemy) and ent.rect.colliderect(target.rect):
                        target.health -= 1
                        ent.health = 0

    @staticmethod
    def verify_health(entity_list: list):
        to_remove = []
        for ent in entity_list:
            if hasattr(ent, 'health') and ent.health <= 0:
                to_remove.append(ent)

        for ent in to_remove:
            entity_list.remove(ent)
