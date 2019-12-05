"""Classes that extend native click classes."""
import click


class CliGroup(click.Group):
    """Extends the use of click.Group.

    This class is used to parse args from cli entry point.

    """

    def invoke(self, ctx: click.Context) -> None:
        """Replace invoke command to pass along args."""
        if ctx.obj is None:
            ctx.obj = tuple(ctx.args)
        else:
            ctx.obj.args = tuple(ctx.args)
        super().invoke(ctx)
