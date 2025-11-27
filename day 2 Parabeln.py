from manim import *

class ParabelAnimation(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-1, 10, 1],
            x_length=9,
            y_length=7,
            axis_config={"include_numbers": True}
        )

        parabola1 = axes.plot(lambda x: x**2, color=BLUE)
        parabola_shifted = axes.plot(lambda x: x**2 + 2, color=YELLOW)
        parabola2 = axes.plot(lambda x: 4*x**2, color=ORANGE)

        label1 = axes.get_graph_label(parabola1, label="y = x^2")
        label2 = axes.get_graph_label(parabola_shifted, label="y = x^2 + 2")
        label3 = axes.get_graph_label(parabola2, label="y = 4x^2")

        self.play(Create(axes))

        graph = parabola1.copy()
        label = label1.copy()

        self.play(Create(graph), Write(label))
        self.wait()

        self.play(
            Transform(graph, parabola_shifted),
            Transform(label, label2),
            run_time=2
        )
        self.wait()

        self.play(
            Transform(graph, parabola2),
            Transform(label, label3),
            run_time=2
        )
        self.wait()

        punkt1 = Dot(axes.c2p(1, 4), color=RED)
        punkt2 = Dot(axes.c2p(1, 0), color=RED)
        punkt3 = Dot(axes.c2p(3,9), color=ORANGE)
        punkt4 = Dot(axes.c2p(0,4), color=RED)
        punkt_label1 = MathTex("(1,4)").next_to(punkt1, UP)
        punkt_label2 = MathTex("(1,0)").next_to(punkt2, UP)
        punkt_label4 = MathTex("(0,4)").next_to(punkt4, LEFT)
        linie1 = Line(punkt1.get_center(), punkt2.get_center(), color=RED)
        linie2 = Line(punkt4.get_center(), punkt1.get_center(), color=RED)
        arrow1 = Arrow(punkt3.get_center(), punkt1.get_center(), color=ORANGE)

        self.play(FadeIn(punkt4), Write(punkt_label4))
        self.play(FadeIn(punkt1), Write(punkt_label1))
        self.play(FadeIn(punkt2), Write(punkt_label2))
        self.play(Create(linie2))
        self.play(Create(linie1))
        self.play(FadeIn(punkt3))
        self.play(Create(arrow1))
        self.wait()
