var buffer_for_drag;

function task_select(e) {
	var temp = document.querySelectorAll('.selected');
	if(temp) {
		temp.forEach( (t) => { t.classList.remove('selected') });
	};
	this.classList.add('selected');
	document.querySelectorAll('.js-tb-btnd').forEach( (btn) => {
		btn.classList.remove('hide');
	});
	form_determ(this.dataset.taskId);
	edit_placehold(this);
};

function task_unselect(e) {
	if(!e.target.classList.contains('js-card') && !e.target.closest('.js-card')) {
		document.querySelectorAll('.js-tb-btnd').forEach( (btn) => {
			btn.classList.add('hide');
		});
		var temp = document.querySelectorAll('.selected');
		if(temp) {
			temp.forEach( (t) => { t.classList.remove('selected') });
		};
	};
};

function drag_strat(e) {
	setTimeout(() => {this.classList.add('hide')}, 0);
	var show_dz = document.querySelectorAll('.js-empty');
	show_dz.forEach( (dz) => { dz.classList.remove('hide') });
	buffer_for_drag = this;
};

function drag_end(e) {
	this.classList.remove('hide');
	var show_dz = document.querySelectorAll('.js-empty');
	show_dz.forEach( (dz) => { dz.classList.add('hide') });
};

function drag_enter(e) {
	let parent_column = e.target.closest('.js-col');
	parent_column.classList.add('hovered');
};

function drop_e(e) {
	var parent_column = this.closest('.js-col');
	var inner = parent_column.querySelector('.js-inner');
	parent_column.classList.remove('hovered');	
	inner.append(buffer_for_drag);
	backend_drop(buffer_for_drag, parent_column);
};

function drag_leave(e) {
	let parent_column = e.target.closest('.js-col');
	parent_column.classList.remove('hovered');
};

function task_manipulation() {
	var cards = document.querySelectorAll('.js-card');
	var drop_zones = document.querySelectorAll('.js-empty');

	window.addEventListener('click', task_unselect);

	drop_zones.forEach((zone) => {
		zone.addEventListener('dragover', function(e) {e.preventDefault()});
		zone.addEventListener('dragenter', drag_enter);
		zone.addEventListener('dragleave', drag_leave);
		zone.addEventListener('drop', drop_e);
	});
	cards.forEach((card) => {
		card.addEventListener('dragstart', drag_strat);
		card.addEventListener('dragend', drag_end);
		card.addEventListener('click', task_select);
	});
	
};

function form_determ(id) {
	var forms = document.querySelectorAll('.js-form-det')
	forms.forEach( (form) => {
		form.querySelector('.js-h-inp').value = id;
	});
};

function edit_placehold(card) {
	var form = document.querySelector('.jsfe');
	form.querySelector('#id_title').value = card.dataset.taskTitle;
	form.querySelector('#id_body').value = card.dataset.taskBody;
	form.querySelector('#id_stage').value = card.dataset.taskStage;
	form.querySelector('#id_bg').value = card.dataset.taskColor;
};

function form_manage(clsstr) {
	var temp = document.querySelector('.'+clsstr);
	if (temp.classList.contains('hide')) {
		temp.classList.remove('hide');
	} else {
		temp.classList.add('hide');
	}
};

function backend_drop(card, col) {
	var request = new XMLHttpRequest();
	var url = document.querySelector('.js-tasks').dataset.dropUrl
	var token = document.querySelector('#jshf').querySelector('input').value;
	let json = JSON.stringify({
		id:card.dataset.taskId, 
		stage:col.dataset.columnId,
	});
	request.open('post', url, true);
	request.setRequestHeader('Content-Type', 'application/json');
	request.setRequestHeader('HTTP_X_REQUESTED_WITH', 'XMLHttpRequest');
	request.setRequestHeader('X-CSRFToken', token);
	request.send(json);
	console.log(request);
};


task_manipulation();



