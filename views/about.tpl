% rebase('layout.tpl', title=title, menu=menu, year=year)
<br>
<br>
<svg xmlns="http://www.w3.org/2000/svg" class="d-block user-select-none" width="100%" height="120"
    aria-label="Placeholder: Image cap" focusable="false" role="img" preserveAspectRatio="xMidYMid slice"
    viewBox="0 0 318 180" style="font-size:1rem;text-anchor:middle;border-radius: 15px;font-weight:500;">
    <rect width="100%" height="100%" fill="#ffc15e"></rect>
    <text x="50%" y="50%" fill="#ffffff" dy=".3em">Разработчики</text>
</svg>
<br>
<div class="row justify-content-center row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
    %for dev in developers:
    <div class="card mb-3">
        <h3 class="card-header">{{ dev.name }}</h3>
        <div class="card-body">
            <h5 class="card-title">ФСПО ГУАП С921</h5>
            <h6 class="card-subtitle text-muted">{{ dev.description }}</h6>
        </div>
        <img src="{{ dev.image_link }}">
        <ul class="list-group list-group-flush">
            <li class="list-group-item">{{ dev.caption_1 }}</li>
            <li class="list-group-item">{{ dev.caption_2 }}</li>
            <li class="list-group-item">{{ dev.caption_3 }}</li>
        </ul>
        <div class="card-body">
            <form action="{{ dev.github_link }}" target="_blank">
                <button type="submit" class="btn btn-outline-dark">Github</button>
            </form>
        </div>
    </div>
    %end
</div>