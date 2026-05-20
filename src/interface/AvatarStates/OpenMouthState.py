#imports

from .AvatarState import AvatarState

class OpenMouthState(AvatarState):
    def enter_state(self, label):
        self.display_avatar(self.returns_img_path(state="open_mouth"), label)