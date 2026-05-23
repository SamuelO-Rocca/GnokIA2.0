#imports

from .AvatarState import AvatarState

class ThinkingState(AvatarState):
    def enter_state(self, label, _interface):
        self.display_avatar(self.returns_img_path(state="thinking"), label)