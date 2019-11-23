
using System;
using System.Collections.Generic;
using System.Text;
using H3;

public class D00149418a6c5ed15984895ba2d8b2529e32797: H3.SmartForm.SmartFormController
{
    public D00149418a6c5ed15984895ba2d8b2529e32797(H3.SmartForm.SmartFormRequest request): base(request)
    {
    }

    protected override void OnLoad(H3.SmartForm.LoadSmartFormResponse response)
    {
        base.OnLoad(response);
        string uuid = System.Guid.NewGuid().ToString();
    }

    protected override void OnSubmit(string actionName, H3.SmartForm.SmartFormPostValue postValue, H3.SmartForm.SubmitSmartFormResponse response)
    {
        base.OnSubmit(actionName, postValue, response);
        // System.Data.DataTable s = this.Engine.Query.QueryTable(string.Format("select * from I_D001494F14848fab9be241528a2d7fd88f8b0ca9 where parentobjectid = '{0}'",this.Request.BizObjectId), null);  //一行代码执行sql


        // H3.DataModel.BizObject personBoo = H3.DataModel.BizObject.Load(H3.Organization.User.SystemUserId, this.Request.Engine, "D00149418a6c5ed15984895ba2d8b2529e32797", this.Request.BizObjectId, false);
        // string ss = personBoo.Schema.SchemaCode;
        // string obj = this.Request.BizObject["F0000005"] + string.Empty;
        // // postValue.Data["F0000005"] + string.Empty
        // //现场作业附件获取  F0000003
        // H3.DataModel.BizObject personBo = Chuanyun2.QueryObjectId(this.Engine, "D00149432ed1f53de3e4cac9e0e6be1adaeaa1a", "F0000006", obj);
        // //自评申请附件获取  F0000001
        // H3.DataModel.BizObject personBo2 = Chuanyun2.QueryObjectId(this.Engine, "D00149408091318b81744a78d3a6c64957ac414", "F0000003", obj);
        // //外部评审附件获取  F0000005
        // H3.DataModel.BizObject personBo3 = Chuanyun2.QueryObjectId(this.Engine, "D00149457378fe071c34b079bbd8155077701a8", "F0000006", obj);
        // //D001494F14848fab9be241528a2d7fd88f8b0ca9.F0000009
        // // this.Engine.BizObjectManager.CopyFiles(personBo.Schema.SchemaCode, "", "F0000003", personBo.ObjectId,personBoo.Schema.SchemaCode, "", "F0000002", personBoo.ObjectId, true, true);//附件复制
        // //加载字表objectid
        // // H3.DataModel.BizObject zb = personBoo["D001494F14848fab9be241528a2d7fd88f8b0ca9"];
        

        // // string uuid = "";
        // this.Engine.BizObjectManager.CopyFiles(personBo.Schema.SchemaCode, "", "F0000003", personBo.ObjectId,
        //     "D001494F14848fab9be241528a2d7fd88f8b0ca9", "", "F0000009", "16f9fda8-1720-41ea-8231-cc0119d716d5", true, true);//子表附件复制

        if(actionName == "F0000006")
        {

        System.Data.DataTable s = this.Engine.Query.QueryTable(string.Format("select * from I_D001494F14848fab9be241528a2d7fd88f8b0ca9 where parentobjectid = '{0}'",this.Request.BizObjectId), null);  //一行代码执行sql


        // H3.DataModel.BizObject personBoo = H3.DataModel.BizObject.Load(H3.Organization.User.SystemUserId, this.Request.Engine, "D00149418a6c5ed15984895ba2d8b2529e32797", this.Request.BizObjectId, false);
        // string ss = personBoo.Schema.SchemaCode;
        // string obj = this.Request.BizObject["F0000005"] + string.Empty;
        string obj = postValue.Data["F0000005"] + string.Empty;
        //现场作业附件获取  F0000003
        H3.DataModel.BizObject personBo = Chuanyun2.QueryObjectId(this.Engine, "D00149432ed1f53de3e4cac9e0e6be1adaeaa1a", "F0000006", obj);
        //自评申请附件获取  F0000001
        H3.DataModel.BizObject personBo2 = Chuanyun2.QueryObjectId(this.Engine, "D00149408091318b81744a78d3a6c64957ac414", "F0000003", obj);
        //外部评审附件获取  F0000005
        H3.DataModel.BizObject personBo3 = Chuanyun2.QueryObjectId(this.Engine, "D00149457378fe071c34b079bbd8155077701a8", "F0000006", obj);
        //D001494F14848fab9be241528a2d7fd88f8b0ca9.F0000009
        // this.Engine.BizObjectManager.CopyFiles(personBo.Schema.SchemaCode, "", "F0000003", personBo.ObjectId,personBoo.Schema.SchemaCode, "", "F0000002", personBoo.ObjectId, true, true);//附件复制
        //加载字表objectid
        // H3.DataModel.BizObject zb = personBoo["D001494F14848fab9be241528a2d7fd88f8b0ca9"];
        

        // string uuid = "";
        this.Engine.BizObjectManager.CopyFiles(personBo.Schema.SchemaCode, "", "F0000003", personBo.ObjectId,
            "D001494F14848fab9be241528a2d7fd88f8b0ca9", "", "F0000009", "16f9fda8-1720-41ea-8231-cc0119d716d5", true, true);//子表附件复制


//.........................................
            // H3.DataModel.BizObject personBoo1 = H3.DataModel.BizObject.Load(H3.Organization.User.SystemUserId, this.Request.Engine, "D00149418a6c5ed15984895ba2d8b2529e32797", this.Request.BizObjectId, false);
            // //现场作业附件获取  F0000003
            // H3.DataModel.BizObject personBoo2 = Chuanyun2.QueryObjectId(this.Engine, "D00149432ed1f53de3e4cac9e0e6be1adaeaa1a", "F0000006", postValue.Data["F0000005"] + string.Empty);
            // //自评申请附件获取  F0000001
            // H3.DataModel.BizObject personBo2 = Chuanyun2.QueryObjectId(this.Engine, "D00149408091318b81744a78d3a6c64957ac414", "F0000003", postValue.Data["F0000005"] + string.Empty);
            // //外部评审附件获取  F0000005
            // H3.DataModel.BizObject personBo3 = Chuanyun2.QueryObjectId(this.Engine, "D00149457378fe071c34b079bbd8155077701a8", "F0000006", postValue.Data["F0000005"] + string.Empty);

            // this.Engine.BizObjectManager.CopyFiles(personBoo.Schema.SchemaCode, "", "F0000002", personBoo.ObjectId,
            // personBo.Schema.SchemaCode, "", "F0000003", personBo.ObjectId, true, true);//照片复制
            // string   fileInfo = "";
            // string[]   ObjectDataId = { personBo["ObjectId"] + string.Empty, personBo2["ObjectId"] + string.Empty, personBo3["ObjectId"] + string.Empty }; //表单的objectid数组
            // H3.DataModel.BizObjectFileHeader[]   fileobject = this.Request.Engine.BizObjectManager.GetBizObjectFileHeaders(ObjectDataId);
            // if(fileobject != null && fileobject.Length > 0)
            // {
            //     foreach(H3.DataModel.BizObjectFileHeader   item in fileobject)
            //     {
            //         fileInfo += item.FileId + ";";
            //     }
            // }
        }
    }
}
//最新....
        if(actionName == "F0000006")
        {
            string uuid = System.Guid.NewGuid().ToString();
            string ss = "insert into I_D001494F14848fab9be241528a2d7fd88f8b0ca9(objectid,parentobjectid,parentpropertyname,parentindex) values ('{0}','{1}','{2}',{3})";
            string sql = string.Format(ss, uuid,this.Request.BizObjectId,"D001494F14848fab9be241528a2d7fd88f8b0ca9",1);
            this.Engine.Query.QueryTable(sql, null);  //一行代码执行sql
            string obj = postValue.Data["F0000005"] + string.Empty;
            //现场作业附件获取  F0000003
            H3.DataModel.BizObject personBo = Chuanyun2.QueryObjectId(this.Engine, "D00149432ed1f53de3e4cac9e0e6be1adaeaa1a", "F0000006", obj);
            // //自评申请附件获取  F0000001
            // H3.DataModel.BizObject personBo2 = Chuanyun2.QueryObjectId(this.Engine, "D00149408091318b81744a78d3a6c64957ac414", "F0000003", obj);
            // //外部评审附件获取  F0000005
            // H3.DataModel.BizObject personBo3 = Chuanyun2.QueryObjectId(this.Engine, "D00149457378fe071c34b079bbd8155077701a8", "F0000006", obj);
            //D001494F14848fab9be241528a2d7fd88f8b0ca9.F0000009
            this.Engine.BizObjectManager.CopyFiles(personBo.Schema.SchemaCode, "", "F0000003", personBo.ObjectId,
                "D001494F14848fab9be241528a2d7fd88f8b0ca9", "", "F0000009", uuid, true, true);//子表附件复制
        }
                base.OnSubmit(actionName, postValue, response);
    }

