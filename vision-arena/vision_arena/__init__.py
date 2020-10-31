from gym.envs.registration import register

register(
    id='vision_arena-v0',
    entry_point='vision_arena.envs:VisionArena',
)
