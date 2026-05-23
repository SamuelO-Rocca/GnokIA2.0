#imports

from .AvatarState import AvatarState

class OpenedEyeState(AvatarState):
    def enter_state(self, label, interface):
        self.display_avatar(self.returns_img_path(state="eyes_opened"), label)
        interface.after_id = label.after(3000, lambda: interface.start_blinking_animation())
