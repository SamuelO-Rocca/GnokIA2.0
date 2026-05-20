#imports

from .AvatarState import AvatarState

class ClosedEyeState(AvatarState):
    def enter_state(self, label):
        self.display_avatar(self.returns_img_path(state="eyes_closed"), label)