from manim import *

class Day3(Scene):
    def construct(self):

        text1 = MathTex(r"-\frac{1}{2}x^2", font_size=72).scale(0.5).shift(LEFT*6 + UP*3)

 
        axes1 = Axes(
            x_range=[-6, 6, 1],
            y_range=[-13, 1, 1],
            x_length=9,
            y_length=7,
            axis_config={"include_numbers": True}
        ).scale(0.8).shift(DOWN * 0.6)


        tabelle1 = Table(
            table=[
                ["x", "-5", "-4", "-3", "-2", "-1", "0", "1", "2", "3", "4", "5"],
                ["y", "25", "16", "9", "4", "1", "0", "1", "4", "9", "16", "25"],
                ["1/2 y", "12.5", "8", "4.5", "2", "0.5", "0", "0.5", "2", "4.5", "8", "12.5"],
            ],
            element_to_mobject=lambda x: Text(str(x), font_size=32),
        ).scale(0.5).shift(UP * 3).shift(RIGHT * 1.7)


        tabelle2 = Table(
            table=[
                ["x", "-5", "-4", "-3", "-2", "-1", "0", "1", "2", "3", "4", "5"],
                ["-1/2 y", "12.5", "8", "4.5", "2", "0.5", "0", "0.5", "2", "4.5", "8", "12.5"],
            ],
            element_to_mobject=lambda x: Text(str(x), font_size=32),
        ).scale(0.6).shift(UP * 3)

        punkt1 = Dot().next_to(text1, RIGHT)
        punkt2 = Dot().next_to(tabelle1, LEFT).shift(DOWN * 0.6)
        pfeil1 = Arrow(punkt1.get_center(), punkt2.get_center())


        self.play(Write(tabelle1), Write(text1))
        self.play(Create(punkt1), Create(punkt2))
        self.play(Create(pfeil1))
        self.wait(0.7)


        self.play(FadeOut(text1, punkt1, punkt2, pfeil1))


        self.play(Transform(tabelle1, tabelle2), run_time=2)
        self.wait(0.5)


        self.play(Create(axes1))
        self.wait(0.2)


        coords = [
            (-5, -12.5),
            (-4, -8),
            (-3, -4.5),
            (-2, -2),
            (-1, -0.5),
            (0, -0),
            (1, -0.5),
            (2, -2),
            (3, -4.5),
            (4, -8),
            (5, -12.5),
        ]


        dots_on_axes = [Dot(axes1.c2p(x, y), color=BLUE) for x, y in coords]


        for d in dots_on_axes:
            self.play(Create(d), run_time=0.06)

        self.wait(0.5)

        smooth_line = VMobject(color=BLUE, stroke_width=5)
        smooth_line.set_points_smoothly([axes1.c2p(x,y) for x,y in coords])
        self.play(Create(smooth_line), run_time=2)

        self.wait(2)
