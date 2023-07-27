from django.contrib import admin


class ScoreFilter(admin.SimpleListFilter):
    title = "Filter by score!"

    parameter_name = "score"

    def lookups(self, request, model_admin):
        return [
            (9, "9점"),
            (8, "8점"),
            (7, "7점"),
        ]

    def queryset(self, request, querysets):
        score_filter = self.value()
        if score_filter:
            score_filter2 = str(float(score_filter) + 1)
            return (
                querysets.all()
                .filter(
                    scorehist__d_date="2023-07-19",
                    scorehist__score__gte=score_filter,
                    scorehist__score__lt=score_filter2,
                )
                .order_by("-scorehist__score")
            )
