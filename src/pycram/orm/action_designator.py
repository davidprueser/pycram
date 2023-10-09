from typing import Optional

from .base import Base, RobotState, Position, Quaternion
from .object_designator import ObjectDesignator
from ..enums import Arms
from sqlalchemy.orm import Mapped, mapped_column, MappedAsDataclass, relationship
from sqlalchemy import ForeignKey


class Action(MappedAsDataclass, Base):
    """ORM class of pycram.designators.action_designator.ActionDesignator.
    The purpose of this class is to correctly map the inheritance from the action designator class into the database.
    Inheritance is implemented as Joined Table Inheritance (see https://docs.sqlalchemy.org/en/20/orm/inheritance.html)
    """
    __tablename__ = "Action"

    dtype: Mapped[str] = mapped_column(init=False)
    robot_state: Mapped[int] = mapped_column(ForeignKey("RobotState.id"), init=False)
    robot_state_table_entry: Mapped[RobotState] = relationship(init=False)

    __mapper_args__ = {
        "polymorphic_identity": __tablename__,
        "polymorphic_on": "dtype",
    }


class ParkArmsAction(Action):
    """ORM Class of pycram.designators.action_designator.ParkArmsDesignator."""
    __tablename__ = "ParkArms"

    id: Mapped[int] = mapped_column(ForeignKey("Action.id"), primary_key=True, init=False)
    arm: Mapped[Arms] = mapped_column(default=None)

    __mapper_args__ = {
        "polymorphic_identity": __tablename__,
    }

    # def __init__(self, arm: str = None):
    #     super().__init__()
    #     self.arm = arm


class NavigateAction(Action):
    """ORM Class of pycram.designators.action_designator.NavigateAction."""

    __tablename__ = "Navigate"

    id: Mapped[int] = mapped_column(ForeignKey("Action.id"), primary_key=True, init=False)
    position: Mapped[int] = mapped_column(ForeignKey("Position.id", ), default=None)
    position_table_entry: Mapped[Position] = relationship(init=False)
    orientation: Mapped[int] = mapped_column(ForeignKey("Quaternion.id"), default=None)
    orientation_table_entry: Mapped[Quaternion] = relationship(init=False)

    __mapper_args__ = {
        "polymorphic_identity": __tablename__,
    }

    # def __init__(self, position: Optional[int] = None, orientation: Optional[int] = None):
    #     super().__init__()
    #     self.position = position
    #     self.orientation = orientation


class MoveTorsoAction(Action):
    """ORM Class of pycram.designators.action_designator.MoveTorsoAction."""

    __tablename__ = "MoveTorso"

    id: Mapped[int] = mapped_column(ForeignKey("Action.id"), primary_key=True, init=False)
    position: Mapped[Optional[float]] = mapped_column(default=None)

    __mapper_args__ = {
        "polymorphic_identity": __tablename__,
    }

    # def __init__(self, position: Optional[float] = None):
    #     super(MoveTorsoAction, self).__init__()
    #     self.position = position


class SetGripperAction(Action):
    """ORM Class of pycram.designators.action_designator.SetGripperAction."""

    __tablename__ = "SetGripper"

    id: Mapped[int] = mapped_column(ForeignKey("Action.id"), primary_key=True, init=False)
    gripper: Mapped[str]
    motion: Mapped[str]

    __mapper_args__ = {
        "polymorphic_identity": __tablename__,
    }

    # def __init__(self, gripper: str, motion: str):
    #     super(SetGripperAction, self).__init__()
    #     self.gripper = gripper
    #     self.motion = motion


class Release(Action):
    """ORM Class of pycram.designators.action_designator.Release."""

    __tablename__ = "Release"

    id: Mapped[int] = mapped_column(ForeignKey("Action.id"), primary_key=True, init=False)
    gripper: Mapped[str] = mapped_column(init=False)
    object: Mapped[int] = mapped_column(ForeignKey("Object.id"), init=False)
    object_table_entry: Mapped[ObjectDesignator] = relationship(init=False)

    __mapper_args__ = {
        "polymorphic_identity": __tablename__,
    }


class GripAction(Action):
    """ORM Class of pycram.designators.action_designator.GripAction."""

    __tablename__ = "Grip"

    id: Mapped[int] = mapped_column(ForeignKey("Action.id"), primary_key=True, init=False)
    gripper: Mapped[str] = mapped_column(init=False)
    effort: Mapped[float] = mapped_column(init=False)
    object: Mapped[int] = mapped_column(ForeignKey("Object.id"), init=False)
    object_table_entry: Mapped[ObjectDesignator] = relationship(init=False)
    # TODO grasped_object

    __mapper_args__ = {
        "polymorphic_identity": __tablename__,
    }


class PickUpAction(Action):
    """ORM Class of pycram.designators.action_designator.PickUpAction."""

    __tablename__ = "PickUp"

    id: Mapped[int] = mapped_column(ForeignKey("Action.id"), primary_key=True, init=False)
    arm: Mapped[str]
    grasp: Mapped[str]
    object: Mapped[int] = mapped_column(ForeignKey("Object.id"), init=False)
    object_table_entry: Mapped[ObjectDesignator] = relationship(init=False)

    __mapper_args__ = {
        "polymorphic_identity": __tablename__,
    }

    # def __init__(self, arm: str, grasp: str):
    #     super(PickUpAction, self).__init__()
    #     self.arm = arm
    #     self.grasp = grasp


class PlaceAction(Action):
    """ORM Class of pycram.designators.action_designator.PlaceAction."""

    __tablename__ = "Place"

    id: Mapped[int] = mapped_column(ForeignKey("Action.id"), primary_key=True, init=False)
    arm: Mapped[str]
    position: Mapped[int] = mapped_column(ForeignKey("Position.id"), init=False)
    position_table_entry: Mapped[Position] = relationship(init=False)
    orientation: Mapped[int] = mapped_column(ForeignKey("Quaternion.id"), init=False)
    orientation_table_entry: Mapped[Quaternion] = relationship(init=False)
    object: Mapped[int] = mapped_column(ForeignKey("Object.id"), init=False)
    object_table_entry: Mapped[ObjectDesignator] = relationship(init=False)

    __mapper_args__ = {
        "polymorphic_identity": __tablename__,
    }

    # def __init__(self, arm: str):
    #     super(PlaceAction, self).__init__()
    #     self.arm = arm


class TransportAction(Action):
    """ORM Class of pycram.designators.action_designator.TransportAction."""

    __tablename__ = "Transport"

    id: Mapped[int] = mapped_column(ForeignKey("Action.id"), primary_key=True, init=False)
    arm: Mapped[str] = mapped_column(init=False)
    position: Mapped[int] = mapped_column(ForeignKey("Position.id"), init=False)
    position_table_entry: Mapped[Position] = relationship(init=False)
    orientation: Mapped[int] = mapped_column(ForeignKey("Quaternion.id"), init=False)
    orientation_table_entry: Mapped[Quaternion] = relationship(init=False)
    object: Mapped[int] = mapped_column(ForeignKey("Object.id"), init=False)
    object_table_entry: Mapped[ObjectDesignator] = relationship(init=False)

    __mapper_args__ = {
        "polymorphic_identity": __tablename__,
    }


class LookAtAction(Action):
    """ORM Class of pycram.designators.action_designator.LookAtAction."""

    __tablename__ = "LookAt"

    id: Mapped[int] = mapped_column(ForeignKey("Action.id"), primary_key=True, init=False)
    position: Mapped[int] = mapped_column(ForeignKey("Position.id"), init=False)
    position_table_entry: Mapped[Position] = relationship(init=False)

    __mapper_args__ = {
        "polymorphic_identity": __tablename__,
    }


class DetectAction(Action):
    """ORM Class of pycram.designators.action_designator.DetectAction."""

    __tablename__ = "Detect"

    id: Mapped[int] = mapped_column(ForeignKey("Action.id"), primary_key=True, init=False)
    object: Mapped[int] = mapped_column(ForeignKey("Object.id"), init=False)
    object_table_entry: Mapped[ObjectDesignator] = relationship(init=False)

    __mapper_args__ = {
        "polymorphic_identity": __tablename__,
    }


class OpenAction(Action):
    """ORM Class of pycram.designators.action_designator.OpenAction."""

    __tablename__ = "Open"

    id: Mapped[int] = mapped_column(ForeignKey("Action.id"), primary_key=True, init=False)
    arm: Mapped[str] = mapped_column(init=False)
    distance: Mapped[float] = mapped_column(init=False)
    object: Mapped[int] = mapped_column(ForeignKey("Object.id"), init=False)
    object_table_entry: Mapped[ObjectDesignator] = relationship(init=False)

    __mapper_args__ = {
        "polymorphic_identity": __tablename__,
    }


class CloseAction(Action):
    """ORM Class of pycram.designators.action_designator.CloseAction."""
    __tablename__ = "Close"
    id: Mapped[int] = mapped_column(ForeignKey("Action.id"), primary_key=True, init=False)
    arm: Mapped[str] = mapped_column(init=False)

    __mapper_args__ = {
        "polymorphic_identity": __tablename__,
    }
