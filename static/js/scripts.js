var buffer_for_drag;

/*
function task_save_or_cancel(e) {
	let wrap = document.querySelector('.js-btns-wrap-sc');
	wrap.classList.remove('hide');
	var sb = wrap.querySelector('.js-btn-save');
	var cb = wrap.querySelector('.js-btn-cancel');
	cb.onclick = () => { location.reload()};
	sb.onclick = () => { 
		wrap.classList.add('hide');
	};

};
*/
function task_select(e) {
	var temp = document.querySelectorAll('.selected');
	if(temp) {
		temp.forEach( (t) => { t.classList.remove('selected') });
	};
	this.classList.add('selected');
	document.querySelectorAll('.js-tb-btnd').forEach( (btn) => {
		btn.classList.remove('disabled');
	});
};

function task_unselect(e) {
	if(!e.target.classList.contains('js-card') && !e.target.closest('.js-card')) {
		document.querySelectorAll('.js-tb-btnd').forEach( (btn) => {
			btn.classList.add('disabled');
		});
		var temp = document.querySelectorAll('.selected');
		if(temp) {
			temp.forEach( (t) => { t.classList.remove('selected') });
		};
	};
};


function create_request() {
	let data = {};
	let cols = document.querySelectorAll('.js-col');
	cols.forEach( (col) => {
		let task_list = [];
		let cards = col.querySelectorAll('.js-card');
		cards.forEach( (card) => {
			task_list.push(card.dataset.taskId)
		});
		data[col.dataset.columnId] = task_list;
	});
	return JSON.stringify(data)
};


function create_object(buff) {
	let str = buff;
	let temp = document.createElement('div');
	temp.innerHTML = str;
	return temp.firstChild;
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






function form_manage(clsstr, m=0) {
	var temp = document.querySelector('.'+clsstr);
	if (!document.querySelectorAll('.disabled').length) {
		if (temp.classList.contains('hide')) {
			temp.classList.remove('hide');
		};	
	};
	if (m) {
		temp.classList.add('hide');
	};
};




















task_manipulation();


