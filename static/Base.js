
			function toLogout(){
				window.location.href='/logout'; 
			}
			function toPraise(obj){
				var ada = {};
				words = obj.attr("id").split("-");
				ada['canteen']=words[0];
				ada['dish']=words[1];
				$.post("/praise",ada,function(data,status){
					obj.attr("onclick","toDelete($(this));");
				obj.html("取消");
				$('#my-dish').append("<li id='"+words[0]+'-'+words[1]+"'><a href='/dish/"+words[1]+"'>"+words[1]+"</a>——<a href='canteen/"+words[0]+"'>"+words[0]+"</li>")
				});
				
			}
			function toDelete(obj){
				var ada = {};
				words = obj.attr("id").split("-");
				ada['canteen']=words[0];
				ada['dish']=words[1];
				$.post("/delete-praise",ada,function(data,status){
					obj.attr("onclick","toPraise($(this));");
				obj.html("赞");
				$("#my-dish #"+words[0]+'-'+words[1]).remove()
				});
				
			}
			function toFindFriend(){
				search_item=$("#search_item").val();
				window.location.href="/search/friend/"+search_item;
			}
			function toFindDish(){
				search_item=$("#search_item").val();
				window.location.href="/search/dish/"+search_item;
			}