from manim import *

class TabelleExample(Scene):
    def construct(self):
        tabel = Table(
            [["x^2", "-3", "-2,5", "-2", "-1,5", "-1", "-0,5", "0", "0.5", "1", "1,5", "2", "2,5", "3"],
             ["y", "9", "6,25", "4", "2,25", "1", "0,25", "0", "0,25", "1", "2,25", "4", "6,25", "9"]]
        ).scale(0.4).shift(UP*2)

        text = Text("(Koordinaten von Punkten)").scale(0.5).next_to(tabel, UP*2)

        self.play(Write(tabel), Write(text), run_time=2) 

        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-1, 10, 1],
            x_length=9,
            y_length=7,
            axis_config={"include_numbers": True}
        ).scale(0.7).shift(DOWN*1.4)

        self.play(Create(axes))

        punkt1 = Dot(axes.c2p(-3,9), color=RED)
        punkt2 = Dot(axes.c2p(-2.5,6.25), color=RED)
        punkt3 = Dot(axes.c2p(-2,4), color=RED)
        punkt4 = Dot(axes.c2p(-1.5,2.25), color=RED)
        punkt5 = Dot(axes.c2p(-1,1), color=RED)
        punkt6 = Dot(axes.c2p(-0.5,0.25), color=RED)
        punkt7 = Dot(axes.c2p(0,0), color=RED)
        punkt8 = Dot(axes.c2p(0.5,0.25), color=RED)
        punkt9 = Dot(axes.c2p(1,1), color=RED)
        punkt10 = Dot(axes.c2p(1.5,2.25), color=RED)
        punkt11 = Dot(axes.c2p(2,4), color=RED)
        punkt12 = Dot(axes.c2p(2.5,6.25), color=RED)
        punkt13 = Dot(axes.c2p(3,9), color=RED)


        self.play(
            FadeIn(punkt1),
            FadeIn(punkt2),
            FadeIn(punkt3),
            FadeIn(punkt4),
            FadeIn(punkt5),
            FadeIn(punkt6),
            FadeIn(punkt7),
            FadeIn(punkt8),
            FadeIn(punkt9),
            FadeIn(punkt10),
            FadeIn(punkt11),
            FadeIn(punkt12),
            FadeIn(punkt13)
            )
        
        linie1 = Line(punkt1.get_center(), punkt2.get_center(), color=RED)
        linie2 = Line(punkt2.get_center(), punkt3.get_center(), color=RED)
        linie3 = Line(punkt3.get_center(), punkt4.get_center(), color=RED)
        linie4 = Line(punkt4.get_center(), punkt5.get_center(), color=RED)
        linie5 = Line(punkt5.get_center(), punkt6.get_center(), color=RED)
        linie6 = Line(punkt6.get_center(), punkt7.get_center(), color=RED)
        linie7 = Line(punkt8.get_center(), punkt7.get_center(), color=RED)
        linie8 = Line(punkt9.get_center(), punkt8.get_center(), color=RED)
        linie9 = Line(punkt10.get_center(), punkt9.get_center(), color=RED)
        linie10 = Line(punkt11.get_center(), punkt10.get_center(), color=RED)
        linie11 = Line(punkt12.get_center(), punkt11.get_center(), color=RED)
        linie12 = Line(punkt13.get_center(), punkt12.get_center(), color=RED)


        self.play(Create(linie1), Create(linie12))
        self.play(Create(linie2), Create(linie11))
        self.play(Create(linie3), Create(linie10))
        self.play(Create(linie4), Create(linie9))
        self.play(Create(linie5), Create(linie8))
        self.play(Create(linie6), Create(linie7))
